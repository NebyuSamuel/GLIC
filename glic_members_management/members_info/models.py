from django.db import models
from datetime import datetime
# Create your models here.
class Profile(models.Model):
    photo = models.ImageField(upload_to='images')
    fullname = models.CharField(max_length=255)
    yearofbirth = models.DateField(default=datetime.now)
    sex = models.CharField(max_length=255, default='Male')
    job = models.CharField(max_length=255, default='No Job')
    subcity = models.CharField(max_length=255, default='xxxx')
    woreda = models.IntegerField(default=0)
    housenum = models.CharField(max_length=255, default='xxxx')
    phonenum = models.CharField(max_length=255, default='xxxx-xx-xx-xx')
    marriage = models.BooleanField(default=False)
    yearofmarriage = models.DateField(default=datetime.now)
    childernnum = models.IntegerField(default=0)
    yearofsalvation = models.DateField(default=datetime.now)
    baptism = models.BooleanField(default=True)
    yearofbaptism = models.DateField(default=datetime.now)
    prevchurch = models.CharField(max_length=255, default = 'GLIC')
    death = models.BooleanField(default=False)
    def __str__(self):
        return self.fullname