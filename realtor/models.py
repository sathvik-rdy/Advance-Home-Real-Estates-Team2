from django.db import models
from django.urls import reverse


# Create your models here.
class realtor(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=250)

    def __str__(self):
        return self.name


