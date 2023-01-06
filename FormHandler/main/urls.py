#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import UsernamePasswordResetForm




urlpatterns = [
    path('', views.index, name="index"),
    path('signup', views.signup, name="signup"),
    path('register', views.register, name="register"),
    path('billing', views.billing, name="billing"),
    path('dashboard/', views.data_page, name="data_page"),
    path('reset_password/', auth_views.PasswordResetView.as_view(form_class=UsernamePasswordResetForm), name='password_reset'),
]   
