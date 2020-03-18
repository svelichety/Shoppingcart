# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 16:33:41 2020

@author: SUNANDA
"""
from django.urls import path
from . import views

#/products
urlpatterns = [
        path('', views.index)
        
        ]