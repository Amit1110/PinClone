from django.db import models
from django.contrib.auth.models import User



class Preferences(models.Model):
	name = models.CharField(max_length = 50)


class Images(models.Model):
	photo = models.ImageField(null=True,blank=True,upload_to='media/')
	tag = models.ForeignKey(Preferences,on_delete = models.CASCADE)

class UserProfile(models.Model):
	user = models.OneToOneField(User,on_delete = models.CASCADE)
	choices = models.ManyToManyField(Preferences)

