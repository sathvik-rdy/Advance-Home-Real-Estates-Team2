# Generated by Django 4.1 on 2022-11-28 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('propertyName', models.TextField(max_length=191, null=True)),
                ('propertyDescription', models.TextField(max_length=500, null=True)),
                ('propertyNeighborhood', models.TextField(max_length=50, null=True)),
                ('propertyZipCode', models.CharField(max_length=10, null=True)),
                ('propertyPrice', models.TextField(max_length=50, null=True)),
                ('propertyImage', models.ImageField(default='default.jpg', upload_to='listings_pics')),
            ],
        ),
    ]
