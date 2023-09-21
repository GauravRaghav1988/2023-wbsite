from django.contrib import admin
from django.urls import path
from .import views
# from myapp.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home),
    path('registration/',views.register),
    path('login/',views.user_login),
    path('account/',views.account), 
    path('changepassword/',views.change_password),
    path('logout/',views.logoutuser),   
    path('quiz/',views.quiz_home,name='quiz_home'),
    path('add_question/',views.addQuestion,name='addQuestion'),
 
]


