from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('signup/', views.signup, name='signup'),
    path('login/', views.signin, name='login'),  
    path('landing/', views.landing, name='landing'),
    path('register_doctor/', views.register_doctor, name='register_doctor'),
    path('doctor_login/', views.doctor_login, name='doctor_login'),
    path('doctor_dashboard/', views.doctor_dashboard, name='doctor_dashboard'),
    path('logout/', views.doctor_logout, name='logout'),
    path('doctor/', views.doctor, name='doctor'),

 ]
