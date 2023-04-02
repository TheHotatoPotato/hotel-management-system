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
    path('hotel_dashboard/', views.hotel_dashboard, name='hotel_dashboard'),
    path('book_room/', views.book_room, name='book_room'),
    path('update_booking/<str:pk>', views.update_booking, name='update_booking'),
    path('delete_booking/<str:pk>', views.delete_booking, name='delete_booking'),
    path('checkout/<str:pk>', views.checkout, name='checkout'),
    path('bookings/', views.bookings, name='bookings'),
] 