from django.db import models
# from django.db.models import Max
def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)

class Employee(models.Model):
    user_id = models.IntegerField(null=False)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length = 500)
    password = models.CharField(max_length=500)
    # role = models.CharField(max_length=100,default="teacher")
    check_in = models.CharField(max_length = 20,default="false")
    check_out = models.CharField(max_length = 20,default="false")
    profile_image_1 = models.FileField(upload_to = 'images/',null=True)
    profile_image_2 = models.FileField(upload_to = 'images/',null=True)
    employee_id =  models.CharField(max_length=1000)





# class Student(models.Model):
#     user_id = models.IntegerField(null=True)
#     name = models.CharField(max_length=50)
#     email = models.EmailField(max_length=500)
#     password = models.CharField(max_length=500)
#     role = models.CharField(max_length=100,default="student")

# def nameFile(instance, filename):
#     return '/'.join(['images', str(instance.name), filename])
    
# class UploadImage(models.Model):  
#     user_id = models.IntegerField(null=True)  
#     image_url = models.ImageField(upload_to='images')   
    





