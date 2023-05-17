from django.db import models
from datetime import date
from django.contrib.auth.models import User

# Create your models here.
class Todo (models.Model):
    created_at=  models.DateField( default=date.today);
    title= models.CharField(max_length=500)
    description=models.CharField(max_length=500)
    user= models.ForeignKey(User, on_delete=models.CASCADE,default=None)