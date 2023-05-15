from django.contrib import admin
from .models import Student #model에 있는 Post를 admin에 불러옴

admin.site.register(Student)#어드민 등록

# Register your models here.
