#Django_prj에서 형식 가져옴
from django.contrib import admin
from django.urls import path, include
from . import  views #views 파일을 가져와 사용하겠다 라는 뜻 (추가해주기)


urlpatterns = [
    path('about_me/', views.about_me),#about_me와 landing은 function 형태 따라서 views에서 함수 추가하기
    path('', views.landing)
]