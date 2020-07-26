# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


# from django.contrib.auth.decorators import login_required

from django.contrib.auth import views as auth_views
#from django.contrib.auth.views import password_reset,password_reset_done,password_reset_confirm,password_reset_complete
from django.contrib.auth.views import PasswordResetDoneView,PasswordResetView,PasswordResetCompleteView,PasswordResetConfirmView

from apps.socio.views import (
    Perfil_Actualizar,
)
 

from .views import (
    registration_view,
    logout_view,
    login_view,
    account_view,
)



urlpatterns = [


#doc registro cambio de password y login
# https://docs.djangoproject.com/en/2.2/topics/auth/default/#module-django.contrib.auth.view
#https://www.youtube.com/watch?v=qjlZWBbX7-o&feature=youtu.be

# Source
# https://github.com/mitchtabian/CodingWithMitch-Blog-Course/tree/Reset-Password-and-Change-Password-(Django)

    path('register/', registration_view, name="register"),
    path('logout/', logout_view, name="logout"),
    path('login', login_view, name="login"),

    # path('account/', account_view, name="account"),
    
    # Password reset links (ref: https://github.com/django/django/blob/master/django/contrib/auth/views.py)
 #@   path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), 
 #@      name='password_change_complete'),
 #@   path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'), 
 #@       name='password_change'),

     path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), 
        name='password_change_complete'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'), 
        name='password_change'),
    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'),
     name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    

    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    

    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
     name='password_reset_complete'),





]





