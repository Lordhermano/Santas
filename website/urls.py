from django.contrib import admin
from django.urls import path, include
from  . import views

urlpatterns = [
    path('',views.display_cards, name='home'),
    path('register',views.register,name='register'),
    path('login',views.login_page,name='login'),
    path('logout',views.logout,name='logout'),
    path('book',views.book,name='book')
]