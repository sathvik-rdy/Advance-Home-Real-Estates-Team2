# Generated by Django 4.1 on 2022-12-02 01:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_rename_firstname_profile_first_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='first_Name',
            new_name='First_Name',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='lastName',
            new_name='Last_Name',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='officeEmail',
            new_name='Office_Email',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='phoneNumber',
            new_name='Phone_Number',
        ),
    ]
