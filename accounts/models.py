from django.db import models
from django.contrib.auth.models import User



class Preference(models.Model):
	name = models.CharField(max_length = 50)

	def __str__(self):
		return self.name


class Image(models.Model):
	photo = models.ImageField(null=True,blank=True,upload_to='media/')
	tag = models.ForeignKey(Preference,on_delete = models.CASCADE)

	def __str__(self):
		return self.photo.name[6:]


class UserProfile(models.Model):
	user = models.OneToOneField(User,on_delete = models.CASCADE)
	choices = models.ManyToManyField(Preference)

	def __str__(self):
		return self.user.username
