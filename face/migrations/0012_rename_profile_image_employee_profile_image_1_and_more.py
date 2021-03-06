# Generated by Django 4.0.5 on 2022-06-24 06:45

from django.db import migrations, models
import face.models


class Migration(migrations.Migration):

    dependencies = [
        ('face', '0011_alter_employee_profile_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='profile_image',
            new_name='profile_image_1',
        ),
        migrations.AddField(
            model_name='employee',
            name='profile_image_2',
            field=models.ImageField(null=True, upload_to=face.models.upload_to),
        ),
    ]
