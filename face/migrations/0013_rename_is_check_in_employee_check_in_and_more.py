# Generated by Django 4.0.5 on 2022-06-24 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('face', '0012_rename_profile_image_employee_profile_image_1_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='is_check_in',
            new_name='check_in',
        ),
        migrations.AddField(
            model_name='employee',
            name='check_out',
            field=models.CharField(default='false', max_length=20),
        ),
    ]
