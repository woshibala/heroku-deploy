from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.
class Article(models.Model):
	title = models.CharField(max_length = 100)
	category = models.CharField(max_length = 50,blank=True)
	date_time = models.DateTimeField(default = timezone.now())
	content = models.TextField(blank =True,null=True)
	username = models.CharField(max_length = 100,default='SOME STRING')
	image = models.ImageField(upload_to='photos', blank=True,null=True)

	def __str__(self):
		return self.title

class User(models.Model):
	username = models.CharField(max_length = 100,default='SOME STRING')
	email = models.EmailField(max_length = 254)
	password = models.CharField(max_length=100)
	user_id = models.BigIntegerField(default = -1)


	def __str__(self):
		return self.username