from django.shortcuts import render, redirect 
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
import json
import os
import zipfile
import urlquote


def index(request):
	context = {}
	return render(request,'index.html', context)

def install(request):
	context = {}
	return render(request,'install.html', context)

@login_required(login_url = 'login')
def user(request, pk_test):
	user = User.objects.get(id = pk_test)
	context = {}
	if request.user.id == user.id:
		devices = user.device_set.all()
		device_count = devices.count()
		context = {"device_count": device_count}
		return render(request,'user.html', context)
	else:
		return render(request,'error.html', context)

@login_required(login_url = 'login')
def devices(request):
	if request.method == 'POST':
			user = User.objects.get(id = request.user.id)
			info = request.POST.get('info')
			info = json.loads(info)
			smart_attr = request.POST.get('smart')
			if not Device.objects.filter(user = user, serialNumber = info.get("Serial Number")):	
				device = Device(user = user, serialNumber = info.get("Serial Number"), modelFamily = info.get("Model Family"), deviceModel = info.get("Device Model"),
					userCapacity = info.get("User Capacity"), sectorSizes = info.get("Sector Sizes"), rotationRate = info.get("Rotation Rate"), ataVersion = info.get("ATA Version is"))
				device.save()
			smart_attr = json.loads(smart_attr)
			device = Device.objects.get(user = user, serialNumber = info.get("Serial Number"))
			for i in range(0,len(smart_attr)-1):
				attr = smart_attr[i]
				if Smartctl.objects.filter(device = device, Num = attr.get("Id")):
					smart = Smartctl.objects.get(device = device, Num = attr.get("Id"))
					
				else:
					smart = Smartctl(device = device, Num = attr.get("Id"), Name = attr.get("Name"), Trash = attr.get("Trash"))
					smart.save()
				attribute = Attribute(smartctl = smart, Current = attr.get("Current"), Type = attr.get("Type"), RawValue = attr.get("RawValue"))
				attribute.save()	

			return HttpResponse(status=200)
	else:
		pk_test = request.user.id
		user = User.objects.get(id = pk_test)
		devices = user.device_set.all() 
		smart_attr = []
		for device in devices:
			for attr in device.smartctl_set.all():
				smart_attr.append((attr,attr.attribute_set.all()[0]))
		context = {"devices": devices, "smart": smart_attr}
		return render(request,'devices.html', context)

def support(request):		
	context = {}
	return render(request,'support.html', context)


def registerPage(request):
	if request.user.is_authenticated:
		return redirect('index')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('login')
			

		context = {'form':form}
		return render(request, 'accounts/register.html', context)


def loginPage(request):
	if request.user.is_authenticated:
		return redirect('index')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')
			user = authenticate(request, username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect('index')
			else:
				messages.info(request, 'Username OR password is incorrect')

	context = {}
	return render(request, 'accounts/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')

def downloadZip(request):

	response = HttpResponse(content_type='application/zip')
	new_zip = zipfile.ZipFile(response, 'w')

	for root, dirs, files in os.walk('./desktop'):
		for file in files:
			new_zip.write(os.path.join(root,file))

	response['Content-Disposition'] = 'attachment; filename="{0}"'.format("desktop.zip")
	return response
