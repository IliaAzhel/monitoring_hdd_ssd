from django.contrib import admin
from .models import Device, Smartctl,Attribute

admin.site.register(Device)
admin.site.register(Smartctl)
admin.site.register(Attribute)