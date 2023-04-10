from django.contrib import admin
from .models import Post #model에 있는 Post를 admin에 불러옴

admin.site.register(Post)#어드민 등록

# Register your models here.
