from django.db import models


class Preferences(models.Model):
	name = models.CharField(max_length = 50)


class Images(models.Model):
	name = models.CharField(max_length = 400)
	photo = models.ImageField(null=True,blank=True)
	tag = models.ForeignKey(Preferences,on_delete = models.CASCADE)


sdkhk