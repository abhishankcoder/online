from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from face.serializers import UserSerializer, GroupSerializer

from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer,RegisterSerializer
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .models import Employee
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
import os






class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserDetailAPI(APIView):
  # authentication_classes = (TokenAuthentication,)
  permission_classes = (AllowAny,)
  def get(self,request,*args,**kwargs):
    user = User.objects.get(id=request.user.id)
    serializer = UserSerializer(user)
    return Response(serializer.data)


#Class based view to register user
class RegisterUserAPIView(generics.CreateAPIView):
  permission_classes = (AllowAny,)
  serializer_class = RegisterSerializer


# @api_view(['POST'])
# def create_teacher(request,formate=None):

#   serializer = TeacherSerializer(data=request.data,many=True)
#   # data = serializer.data

#   if serializer.is_valid():
#     serializer.save()
#     return Response(serializer.data, status=status.HTTP_201_CREATED)
#   else:
#     return Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST)

    # else:
    #   serializer = StudentSerializer(data=request.data)
    #   if serializer.is_valid():
    #     serializer.save()
    #       # Student.objects.create(
    #       #     serializer.init_data['role'],
    #       #     serializer.init_data['email'],
    #       #     serializer.init_data['name'],
    #       #     serializer.init_data['password']
    #       # )
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)
    #   else:
    #     return Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST)

# class cand_Views(APIView):
#     def post(self, request, formate = None):
#         serializer = TeacherSerializer(data=request.data)
#         if serializer.is_valid():
#           serializer.save()
#           return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
#         else:
#           return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

# class CanRegisterApiView(APIView):
#     parser_classes = [JSONParser]
#     def post(self, request,formate=None):
#         serializer = EmployeeSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
            
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
            

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class LoginApiView(APIView):
#     def post(self, request,formate=None):
#         role = request.data['role']
#         costom_id = request.data['id']
#         password = request.data['password']
#         if role == 'teacher':
#             teacher_obj = Teacher.objects.filter(id=costom_id,password=password).first()
#             if teacher_obj:
#                 data = {
#                     "status":"successfully login"
#                 }
#             return Response(data)
#         if role == 'student':
#             stu_obj = Teacher.objects.filter(id=costom_id,password=password).first()
#             if stu_obj:
#                 data = {
#                     "status":"successfully login"
#                 }
#             return Response(data)

#register api
class CanRegister(APIView):
    permission_classes = [permissions.AllowAny]
    parser_classes = [JSONParser]
    # parser_classes = (MultiPartParser, FormParser)
    def post(self, request, format=None):
        username = request.data['username']
        # first_name = request.data['first_name']
        # last_name = request.data['last_name']
        email = request.data['email']
        password = request.data['password']
        # password2 = request.data['password2']
        if password:
            serializer = RegisterSerializer(data=request.data, context={'request': request})
            if serializer.is_valid(raise_exception=True):
                serializer.save()
            user_obj = User.objects.latest('id')
            user_id = user_obj.id
            employee_id = "Emp00" + str(user_id)
            Candidate_obj = Employee.objects.create(user_id=user_id,name=username,email=email,password=password,employee_id=employee_id)
        # else:
        #     Candidate_obj = Student.objects.create(user_id=user_id,name=username,email=email,password=password)
        response = {
                "status_code": 200,
                "message": "User signed up successfully",
                "status": "success",
                "employee_id":employee_id,
                "data": [serializer.data]
            }
        return Response(response)

#login api
class login_employee(APIView):
    parser_classes = (MultiPartParser,FormParser,JSONParser)
    def post(self, request, format=None):

        employee_id = request.query_params.get('employee_id')
        image = request.data['image']
        size = image.size
        name = image.name
        # return Response(name)
        file_extension = os.path.splitext(name)[1][1:]
        # return Response(file)
        Emp_obj = Employee.objects.filter(employee_id=employee_id).update(profile_image_1=image)
        return Response({'message': "login sussefully"}, status=200)

#check in
class checkin(APIView):
    parser_classes = (MultiPartParser,FormParser,JSONParser)
    def post(self, request, format=None):

        employee_id = request.query_params.get('employee_id')
        Emp_obj = Employee.objects.filter(employee_id=employee_id).first()
        if Emp_obj:
            pass 
        else:
            data = {
                "message":"Enter valid Employee id"
            }
            return Response(data)
        image = request.data['image']
        if image:
            pass
        else:
            data = {
                "message":"image is required"
            }
            return Response(data)
        size = image.size
        name = image.name
        # return Response(name)
        file_extension = os.path.splitext(name)[1][1:]

        status = request.data['status']
        # return Response(file)

        Emp_obj = Employee.objects.filter(employee_id=employee_id).update(profile_image_2=image,check_in=status)
        Emp_obj = Employee.objects.filter(employee_id=employee_id).first()
        path1 = Emp_obj.profile_image_1.path
        path2 = Emp_obj.profile_image_2.path
        # return Response()
        import cv2
        import face_recognition
        try:
            gambar1= face_recognition.load_image_file(path1)
            gambar1 = cv2.cvtColor(gambar1, cv2.COLOR_BGR2RGB)
            L1 = face_recognition.face_locations(gambar1)[0]
            en1 = face_recognition.face_encodings(gambar1)[0]
            k1 = cv2.rectangle(gambar1,(L1[3],L1[0]),(L1[1],L1[2]),(255,0,0),2)
            gambar2 = face_recognition.load_image_file(path2)
            gambar2 = cv2.cvtColor(gambar2, cv2.COLOR_BGR2RGB)
            L2 = face_recognition.face_locations(gambar2)[0]
            en2 = face_recognition.face_encodings(gambar2)[0]
            k2 = cv2.rectangle(gambar2,(L2[3],L2[0]),(L2[1],L2[2]),(255,0,0),2)
            nasil = face_recognition.compare_faces([en1],en2)
            pers = face_recognition.face_distance([en1],en2)
            return Response({'message': "check in sussefully"}, status=200)
        except:
            return Response({'message': "try again"}, status=200)


class checkout(APIView):
    parser_classes = (MultiPartParser,FormParser,JSONParser)
    def post(self, request, format=None):

        employee_id = request.query_params.get('employee_id')
        Emp_obj = Employee.objects.filter(employee_id=employee_id).first()
        if Emp_obj:
            pass 
        else:
            data = {
                "message":"Enter valid Employee id"
            }
            return Response(data)
        image = request.data['image']
        if image:
            pass
        else:
            data = {
                "message":"image is required"
            }
            return Response(data)
        size = image.size
        name = image.name
        # return Response(name)
        file_extension = os.path.splitext(name)[1][1:]

        status = request.data['status']
        # return Response(file)

        Emp_obj = Employee.objects.filter(employee_id=employee_id).update(profile_image_2=image,check_in=status)
        return Response({'message': "check out sussefully"}, status=200)