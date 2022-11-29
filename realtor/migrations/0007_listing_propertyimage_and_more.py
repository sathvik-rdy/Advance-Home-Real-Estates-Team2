# Generated by Django 4.1 on 2022-11-28 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtor', '0006_remove_listing_propertyimage_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='propertyImage',
            field=models.ImageField(default='default.jpg', upload_to='listings_pics'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='propertyDescription',
            field=models.TextField(max_length=100, null=True),
        ),
        migrations.DeleteModel(
            name='Images',
        ),
    ]