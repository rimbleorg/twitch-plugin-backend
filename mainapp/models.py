from django.db import models

# Create your models here.

class BroadCastId(models.Model):
	username = models.CharField(max_length=100)
	broadcast_id = models.CharField(max_length=100)
	access_code = models.CharField(max_length=100)

