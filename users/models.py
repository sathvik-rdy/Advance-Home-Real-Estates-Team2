from PIL import Image
from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    firstName = models.CharField(max_length = 25, null = True)
    lastName  = models.CharField(max_length = 25, null = True)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')
    phoneNumber = models.CharField(max_length=13, null=True)
    address = models.TextField(max_length = 200, null = True)
    officeEmail = models.EmailField(max_length = 50,null = True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args,**kwargs):
        super().save(*args,**kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width >300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
