# Generated by Django 4.0.5 on 2022-06-23 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('face', '0006_remove_student_image_remove_teacher_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(null=True)),
                ('image', models.ImageField(upload_to='images')),
            ],
        ),
    ]
