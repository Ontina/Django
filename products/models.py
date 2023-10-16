from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Food(models.Model):
  title = models.CharField(max_length=50)
  Description = models.TextField(max_length=50)
  Photo = models.ImageField(upload_to='food')
  Dateuploaded = models.DateField(auto_now_add=True)
  active = models.BooleanField(default=True)
  user = models.ForeignKey(User, on_delete=models.RESTRICT)
  amount = models.DecimalField(max_digits=5, decimal_places=2)
