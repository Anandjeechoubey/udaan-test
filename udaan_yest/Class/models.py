from User.models import user
from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.

choices=[("G","Gym"),("Y","Yoga"),("D","Dance"),]


class Class(models.Model):
    type=models.CharField(choices=choices,default=choices[0],max_length=255)
    capacity=models.IntegerField(blank=True,null=True)
    studentlist=models.ArrayField(user,max_length=capacity,on_delete=models.CASCADE)
    waitinglist=models.ArrayField(user,max_length=10,on_delete=models.CASCADE)