from django.db import models

# Create your models here.
class User(models.Model):
  fname = models.CharField(max_length=50)
  lname = models.CharField(max_length=50)
  email = models.EmailField(unique=True)
  age = models.IntegerField(default=18)
  active = models.BooleanField(default=True)
  photo = models.FileField(upload_to="profile")
  photo = models.ImageField(upload_to="profile")
  dateregister = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  aboutme= models.TextField()