#Django_prj url에서 형식 가져옴
from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index),
    path('prob/', views.St_List.as_view()),
    path('prob/<int:pk>/', views.St_Detail.as_view()),
]