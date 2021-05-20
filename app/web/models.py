from django.db import models
from django.contrib.auth.models import User

class Device(models.Model):
	user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
	serialNumber = models.CharField(max_length = 40, help_text = "serialNumber",default = "num")
	modelFamily = models.CharField(max_length = 50, help_text = "ModelFamily",null = True)
	deviceModel = models.CharField(max_length = 40, help_text = "DeviceModel",null = True)
	userCapacity = models.CharField(max_length = 40, help_text = "UserCapacity",null = True)
	sectorSizes = models.CharField(max_length = 40, help_text = "SectorSizes",null = True)
	rotationRate = models.CharField(max_length = 40, help_text = "Rotation Rate",null = True)
	ataVersion = models.CharField(max_length = 40, help_text = "ATA Version is", default = "ata")

	#temperature = models.CharField(max_length = 20, help_text = "Device temperature")
	#health = models.CharField(max_length = 20, help_text = "Device state")
	#pc_name = models.CharField(max_length = 20, help_text = "PC name")
	#last_update = models.DateField(null = True, blank = True)
	
	#DEVICE_TYPE = (
	#	('S','SSD'),
	#	('H','HDD')
	#)

	#type_of_device = models.CharField(max_length = 1,choices = DEVICE_TYPE, blank = True, default = 'HDD', help_text = "SSD or HDD")

	def __str__(self):

		return '%s (%s)' % (self.id, self.serialNumber)

class Smartctl(models.Model):
	
	device = models.ForeignKey(Device, on_delete=models.SET_NULL, null=True, blank=True)
	Num = models.CharField(max_length = 30, help_text= "Id",default= "ID")
	Name = models.CharField(max_length = 30, help_text= "Name",null = True)
	Current = models.CharField(max_length = 30, help_text= "Current",null = True)
	Trash = models.CharField(max_length = 30, help_text= "Trash",null = True)
	Type = models.CharField(max_length = 30, help_text= "Type",null = True)
	RawValue = models.CharField(max_length = 30, help_text= "RawValue",null = True)

	def __str__(self):

		return '%s (%s)' % (self.id, self.Name)	

