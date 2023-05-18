from django.db import models
from django.contrib.auth.models import User
from user_profile.models import UserProfile

class Experience(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, default='')
	company = models.CharField(max_length=200)
	role = models.CharField(max_length=200)
	startDate = models.DateField()
	endDate = models.DateField()
	description = models.CharField(max_length=500)

	def __str__(self):
		return self.company

class Education(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, default='')
	school = models.CharField(max_length=200)
	degree = models.CharField(max_length=200)
	startDate = models.DateField()
	endDate = models.DateField()
	description = models.CharField(max_length=500)

	def __str__(self):
		return self.school

class Skill(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, default='')
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name