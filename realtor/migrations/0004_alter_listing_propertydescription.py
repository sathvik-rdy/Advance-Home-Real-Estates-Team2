# Generated by Django 4.1 on 2022-11-28 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtor', '0003_alter_listing_propertydescription_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='propertyDescription',
            field=models.CharField(max_length=100, null=True),
        ),
    ]