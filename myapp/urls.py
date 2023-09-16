from django.contrib import admin
from django.urls import path
from .import views
# from .views import create_user, users_list,courses_list,create_course



urlpatterns = [
    path('',views.home),
    # path('about/',views.about),
    # # path('records/',views.records),
    # path('registration/',views.register),
    # path('login/',views.user_login),
    # path('success/',views.success),
    # path('account/',views.account), 
    # path('changepassword/',views.change_password),
    # path('logout/',views.logoutuser),
    
]
