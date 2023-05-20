import os

from django.db import models
from django.contrib.auth.models import User #장고에서 기본으로 만든 유저 테이블
# Create your models here.

class Tag(models.Model): #Tag db
    name = models.CharField(max_length=50, unique=True)  # unique 겹치지 않게하는것
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)  # 주요단어(타이틀로 쓸 수 있는것),unicode 한글가능

    def __str__(self):
        return self.name
class Category(models.Model): #카테고리 db테이블 만들기
    name = models.CharField(max_length=50, unique=True) #unique 겹치지 않게하는것
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True) #주요단어(타이틀로 쓸 수 있는것),unicode 한글가능

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return f'/blog/category/{self.slug}/'  #f''는 문자열을 만드는 함수 #self.pk는 해당객체의 primary key

    class Meta:
        verbose_name_plural = 'Categories' #어드민 사이트 이름 변경하기

class Post(models.Model): #일종의 db구조 , field설정
    title = models.CharField(max_length=30)
    hook_text = models.CharField(max_length=100, blank=True)#검색어를 넣을 수 있는 필드 blank=true(필수항목x)
    contents = models.TextField()

    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True) #blank=true는 필수 항목이 아니라는것을 의미
    file_upload = models.FileField(upload_to='blog/files/%Y/%m/%d/', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #author
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)#models.CASCADE를 하면 포스트도 지워짐

    #1대 다 일때 foreignkey
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)#카테고리 지정하기

    # 다대 다 관계 ManyToManyField
    tags = models.ManyToManyField(Tag, blank=True)  # 카테고리 지정하기

    #{self.pk} : 타이틀의 앞에다가 번호를 붙여줌 프라이머리 키 의미.
    #{self.title} : 내가 설정한 타이틀로 제목을 설정해줌ㅂ

    def __str__(self):
        return f'[{self.pk}]{self.title} :: {self.author}'

    #index.html에 사용되는 함수 (블로그 링크 관력)
    def get_absolute_url(self):
        return f'/blog/{self.pk}/'  #f''는 문자열을 만드는 함수 #self.pk는 해당객체의 primary key

    def get_file_name(self):
        return os.path.basename(self.file_upload.name)

    def get_file_ext(self):
        return self.get_file_name().split('.')[-1] #(test.txt ..ttt.final.real.doc 일 경우 점을 기준해 쪼개라)
                                                   #[-1]이기때문에 마지막 .을 가져와서 리턴하는 함수
