from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('register/', views.registerHotel, name='register'),
    path('login/', views.loginHotel, name='login'),
    path('logout/', views.logoutHotel, name='logout'),
    path('change_password/', views.change_password, name='change_password'),
    path('hotel_application/', views.hotel_application, name='hotel_application'),
    path('hotel_statistics/', views.hotel_statistics, name='hotel_statistics'),
] 