from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Event(models.Model):
	#Event author - link to Users
	#author = models.ForeignKey(User,)
	#Event title
	title = models.CharField(max_length= 120,null=True,blank=True)
	#Event description - text field
	description = models.CharField(max_length=1000,verbose_name=u'Краткое описание',default=None)
	#Event date range
	startDate = models.DateTimeField(verbose_name=u'Дата начала',auto_now=False, auto_now_add=False)
	endDate = models.DateTimeField(verbose_name=u'Дата окончания',auto_now=False, auto_now_add=False,null=True,blank=True)
	date_created = models.DateTimeField(verbose_name=u'Дата создания',auto_now_add=True)

	#Event participants - link to Users, get from SN api's?

	class Meta:
		ordering=['-date_created']
		verbose_name = 'Событие'
		verbose_name_plural = 'События'

	
