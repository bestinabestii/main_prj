"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('admin_login', views.admin_login, name='admin_login'),
    path('admin_changepassword', views.admin_changepassword, name='admin_changepassword'),
    path('admin_logout', views.admin_logout, name='admin_logout'),
    path('admin_home', views.admin_home, name='admin_home'),

    path('distadmin_login', views.distadmin_login, name='distadmin_login'),
    path('distadmin_home', views.distadmin_home, name='distadmin_home'),
    path('distadmin_changepassword', views.distadmin_changepassword, name='distadmin_changepassword'),
    path('distadmin_logout', views.distadmin_logout, name='distadmin_logout'),

    path('official_login', views.official_login, name='official_login'),
    path('official_home', views.official_home, name='official_home'),
    path('official_changepassword', views.official_changepassword, name='official_changepassword'),
    path('official_logout', views.official_logout, name='official_logout'),

    path('volunteer_login', views.volunteer_login_check, name='volunteer_login'),
    path('volunteer_home', views.volunteer_home, name='volunteer_home'),
    path('volunteer_details_add', views.volunteer_details_add, name='volunteer_details_add'),
    path('volunteer_changepassword', views.volunteer_changepassword, name='volunteer_changepassword'),
    path('volunteer_logout', views.volunteer_logout, name='volunteer_logout'),

    path('user_login', views.user_login_check, name='user_login'),
    path('user_logout', views.user_logout, name='user_logout'),
    path('user_home', views.user_home, name='user_home'),
    path('user_details_add', views.user_details_add, name='user_details_add'),
    path('user_changepassword', views.user_changepassword, name='user_changepassword'),



]
