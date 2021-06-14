from django.db import models

# Create your models here.

class BroadCastId(models.Model):
	access_code = models.CharField(max_length=100)

