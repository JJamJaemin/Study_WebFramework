"""Django_prj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
#path뒤 include 추가
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),#어드민 사이트 연결해주기 admin을 붙였을때 링크되는 위치
    path('', include('single_pages.urls')), #아무것도 붙이지 않으면 single_pages로(single_pages에 urls파일이 없으므로 생성하기)
    path('blog/', include('blog.urls')),#blog를 붙였을때 연결위치(마찬가지로 blog에도 urls파일 생성해주기)

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)