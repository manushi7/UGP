#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('signup', views.signup, name="signup"),
    path('register', views.register, name="register"),
    path('billing', views.billing, name="billing"),
    path('reset_password', views.reset_password, name="password_reset"),
    path('dashboard/', views.data_page, name="data_page"),
]   
