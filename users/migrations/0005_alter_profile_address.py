# Generated by Django 4.1 on 2022-12-02 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_profile_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=models.TextField(max_length=75, null=True),
        ),
    ]
