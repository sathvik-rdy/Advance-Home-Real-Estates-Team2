# Generated by Django 4.1 on 2022-11-27 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_profile_firstname_alter_profile_lastname'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='officeEmail',
            field=models.EmailField(max_length=25, null=True),
        ),
    ]
