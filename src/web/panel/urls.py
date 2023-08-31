# -*- coding: utf-8 -*-

from django.urls import path

from . import views

app_name = 'panel'

urlpatterns = [
     path('dashboard/', views.index_view, name='dashboard'),
]
