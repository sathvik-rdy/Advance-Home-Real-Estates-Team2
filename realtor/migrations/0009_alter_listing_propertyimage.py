# Generated by Django 4.1 on 2022-12-03 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtor', '0008_alter_listing_propertyimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='propertyImage',
            field=models.ImageField(default='default.jpg', upload_to='listings_pics'),
        ),
    ]
