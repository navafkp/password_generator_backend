from django.db import models

# Create your models here.
from user.models import CustomUser
 
class SavePassword(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    password = models.CharField(max_length=30)
    platform = models.CharField(max_length=30)