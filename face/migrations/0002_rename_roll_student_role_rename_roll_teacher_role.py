# Generated by Django 4.0.5 on 2022-06-23 02:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('face', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='roll',
            new_name='role',
        ),
        migrations.RenameField(
            model_name='teacher',
            old_name='roll',
            new_name='role',
        ),
    ]
