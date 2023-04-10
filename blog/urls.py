#Django_prj url에서 형식 가져옴
from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index),
    path('<int:pk>/', views.single_post_page),#모델을 포함시키는 형태로 만들기 위해 single_pages랑 살짝 다름
        #int:pk는 views.single_post_page 여기에 인자값으로 넘김.
]