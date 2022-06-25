from django.urls import path
from .views import UserDetailAPI,RegisterUserAPIView 
from django.conf.urls.static import static
from .views import (
    CanRegister,login_employee,checkin,checkout,
)
urlpatterns = [
  path("user_details",UserDetailAPI.as_view()),
  path('add_employee',RegisterUserAPIView.as_view()),
  # path("can_signup/", TeacherListApiView.as_view(), name="teach_signup"),
  # path("can_login/", LoginApiView.as_view(), name="teach_login"),

  #register employee--by hr
  path("add_emp/", CanRegister.as_view(), name="teach_login1"),

  # login user/employee
  path('login/', login_employee.as_view(), name='login'),
  
  #checkin/checkout---employee
  # path('login/', login_employee.as_view(), name='login'),
  path('checkin_employee/', checkin.as_view(), name='checkin'),

  #checkout---employee--
  path('checkout_employee/', checkout.as_view(), name='checkout'),
]