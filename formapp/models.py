from django.db import models
from django.utils import timezone
from datetime import datetime


# Create your models here.
class Startup_app_form(models.Model):
	name				    = models.CharField(max_length=100,null=True,blank=True)
	contact				    = models.CharField(max_length=100,null=True,blank=True)
	email 					= models.EmailField(verbose_name="email", max_length=60,null=True,blank=True)
	district				= models.CharField(max_length=100,null=True,blank=True)
	company_name			= models.CharField(max_length=100,null=True,blank=True)
	designation				= models.CharField(max_length=100,null=True,blank=True)
	sector				    = models.CharField(max_length=100,null=True,blank=True)
	date_incorporation		= models.CharField(max_length=100,null=True,blank=True)
	problem_solving			= models.CharField(max_length=1000,null=True,blank=True)
	solution				= models.CharField(max_length=1000,null=True,blank=True)
	uniqueness				= models.CharField(max_length=1000,null=True,blank=True)
	advantages				= models.CharField(max_length=1000,null=True,blank=True)
	operation_stage			= models.CharField(max_length=1000,null=True,blank=True)
	revenue				    = models.CharField(max_length=1000,null=True,blank=True)
	startup_img				= models.ImageField(upload_to='awardimg/',null=True,blank=True)
	vid_link				= models.CharField(max_length=500,null=True,blank=True)
	pitch_startup			= models.CharField(max_length=100,null=True,blank=True)
	folder_file			    = models.FileField(upload_to='pitchfile',null=True,blank=True)

	

	def __str__(self):
		return self.name



class Enterpreneur_form(models.Model):
	name				    = models.CharField(max_length=100,null=True,blank=True)
	contact				    = models.CharField(max_length=100,null=True,blank=True)
	email 					= models.EmailField(verbose_name="email", max_length=60,null=True,blank=True)
	district				= models.CharField(max_length=100,null=True,blank=True)
	company_name			= models.CharField(max_length=100,null=True,blank=True)
	designation				= models.CharField(max_length=100,null=True,blank=True)
	sector				    = models.CharField(max_length=100,null=True,blank=True)
	date_incorporation		= models.CharField(max_length=100,null=True,blank=True)
	location			    = models.CharField(max_length=100,null=True,blank=True)
	turnover				= models.CharField(max_length=100,null=True,blank=True)
	journey				    = models.CharField(max_length=1000,null=True,blank=True)
	achievements			= models.CharField(max_length=1000,null=True,blank=True)
	awards			        = models.CharField(max_length=1000,null=True,blank=True)
	impact				    = models.CharField(max_length=1000,null=True,blank=True)
	vision				    = models.CharField(max_length=1000,null=True,blank=True)
	nomination			    = models.CharField(max_length=1000,null=True,blank=True)

	

	def __str__(self):
		return self.name

class upload(models.Model):
	pdf_file			    = models.FileField(upload_to='pitchfile',null=True,blank=True)
	

class logo(models.Model):
	logo_img				= models.ImageField(upload_to='logo/',null=True,blank=True)