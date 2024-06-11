from django.contrib import admin
from .models import Post ,Category,Tag, Comment #model에 있는 Post를 admin에 불러옴

admin.site.register(Post)#어드민 등록
admin.site.register(Comment)

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)