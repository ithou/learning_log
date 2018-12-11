#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2018/12/10 19:38
# @Author: https://github.com/ithou
"""为程序users定义URL模式"""

from django.urls import path
from django.contrib.auth.views import LoginView

from . import views

app_name = 'users'

urlpatterns = [
    # 登录页面 login
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),

    # 注销页面 logout
    path('logout/', views.logout_view, name='logout'),

    # 注册页面
    path('register/', views.register, name='register')



]

