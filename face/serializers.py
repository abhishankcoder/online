from django.contrib.auth.models import User, Group
# from rest_framework import serializers

from rest_framework import serializers
# from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from .models import Employee

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class RegisterSerializer(serializers.ModelSerializer):
  # email = serializers.EmailField(
  #   required=True,
  #   validators=[UniqueValidator(queryset=User.objects.all())]
  # )
  # password = serializers.CharField(
  #   write_only=True, required=True, validators=[validate_password])
  # password2 = serializers.CharField(write_only=True, required=True)
  class Meta:
    model = User
    fields = ('username', 'password','email')
    # extra_kwargs = {
    # #   'first_name': {'required': True},

    # #   'last_name': {'required': True}
    # }
  # def validate(self, attrs):
  #   if attrs['password'] != attrs['password2']:
  #     raise serializers.ValidationError(
  #       {"password": "Password fields didn't match."})
  #   return attrs
  # def create(self, validated_data):
  #   user = User.objects.create(
  #     username=validated_data['username'],
  #     email=validated_data['email']
  #   #   first_name=validated_data['first_name'],
  #   #   last_name=validated_data['last_name']
  #   )
  #   user.set_password(validated_data['password'])
  #   user.save()
  #   if user:
  #     Emp = Employee.objects.create(
  #     user_id = user.id
  #     Name=user.username,
  #     email=validated_data['email'],
  #     employee_id = "Emp" + str(user_id),
  #     )
  #     Emp.set_password(validated_data['password'])
  #     Emp.save()
  #   return user

class EmployeeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Employee
    fields = ['name', 'email','password']

  # def create(self, validated_data):
  #   user1 = Teacher.objects.create(
  #     name=validated_data['name'],
  #     email=validated_data['email']
  #   #   first_name=validated_data['first_name'],
  #   #   last_name=validated_data['last_name']
  #   )
  #   user1.set_password(validated_data['password'])
  #   user1.save()
  #   return user1

# class StudentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Student
#         fields = ['name', 'email','password','role']

# class ImageUploadSerializer(serializers.ModelSerializer):
#     class Meta:
#       model = UploadImage
#       fields = ['user_id','image_url']
