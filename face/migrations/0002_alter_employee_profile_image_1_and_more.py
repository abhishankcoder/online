# Generated by Django 4.0.5 on 2022-06-24 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('face', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='profile_image_1',
            field=models.FileField(null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='profile_image_2',
            field=models.FileField(null=True, upload_to='images/'),
        ),
    ]