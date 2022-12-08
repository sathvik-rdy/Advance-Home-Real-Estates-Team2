from django.db import models
from django.urls import reverse
from PIL import Image


# Create your models here.
class realtor(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Listing(models.Model):
    propertyName = models.CharField(max_length=50, null=True)
    propertyDescription = models.TextField(max_length=100, null=True)
    propertyAddress = models.CharField(max_length=50, null=True)
    propertyType = models.CharField(max_length=50, null=True)
    propertyNeighborhood = models.CharField(max_length=50, null=True)
    propertyZipCode = models.CharField(max_length=10, null=True)
    propertyPrice = models.CharField(max_length=10, null=True)
    propertyStatus = models.CharField(max_length=15, null=True)
    featuredProperty = models.BooleanField(default=False)
    propertyImage = models.ImageField(default='default.jpg', upload_to='listings_pics')
    #propertyImage = models.FileField()
    def __str__(self):
        return self.propertyName



#class Listing(models.Model):
#    propertyName = models.CharField(max_length=50, null=True)
#    propertyDescription = models.CharField(max_length=100, null=True)
#    propertyNeighborhood = models.CharField(max_length=50, null=True)
#    propertyZipCode = models.CharField(max_length=10, null=True)
#    propertyPrice = models.CharField(max_length=10, null=True)

#    def __str__(self):
#        return self.propertyName

#class Images(models.Model):
#    imageName = models.CharField(max_length=10, null=True)
#    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
#    image = models.ImageField(default='default.jpg', upload_to='listings_pics')

