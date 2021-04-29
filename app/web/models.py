from django.db import models

class Device(models.Model):
	name = models.CharField(max_length = 40, help_text = "Device name")
	temperature = models.CharField(max_length = 20, help_text = "Device temperature")
	health = models.CharField(max_length = 20, help_text = "Device state")
	pc_name = models.CharField(max_length = 20, help_text = "PC name")
	last_update = models.DateField(null = True, blank = True)
	
	DEVICE_TYPE = (
		('S','SSD'),
		('H','HDD')
	)

	type_of_device = models.CharField(max_length = 1,choices = DEVICE_TYPE, blank = True, default = 'HDD', help_text = "SSD or HDD")

	def __str__(self):

		return '%s (%s)' % (self.id, self.name)

class Metadata(models.Model):
	
	device = models.OneToOneField(Device, on_delete=models.CASCADE, primary_key = True,)
	metadata = models.CharField(max_length = 30, help_text= "Metadata")

	def __str__(self):

		return '%s (%s)' % (self.id, self.metadata)	

