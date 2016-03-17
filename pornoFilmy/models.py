from __future__ import unicode_literals
from django.utils import timezone
from django.db import models

# Create your models here.
class Movie(models.Model):
	title = models.CharField(max_length=120)

	def getTitle(self):
		return self.title

	def save(self,title,ID):
		self.title = title
		self.ID = ID
		self.save()

	def sayHello(title):
		print "Hello! " + title