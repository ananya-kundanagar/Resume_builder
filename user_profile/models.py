from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE)
   phone = models.CharField(max_length=25, blank=True)
   profession = models.CharField(max_length=50, blank=True)
   bio = models.TextField(max_length=300, blank=True)
   color = models.CharField(max_length=10, default='green')
   
   def __str__(self):
      return self.user.username