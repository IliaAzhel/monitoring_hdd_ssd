from django.contrib import admin
from .models import Device, Smartctl

admin.site.register(Device)
admin.site.register(Smartctl)