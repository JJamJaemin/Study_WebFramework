from django.db import models

# Create your models here.
class Post(models.Model): #일종의 db구조 , field설정
    title = models.CharField(max_length=30)
    hook_text = models.CharField(max_length=100, blank=True)#검색어를 넣을 수 있는 필드 blank=true(필수항목x)
    contents = models.TextField()

    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True)
    file_upload = models.FileField(upload_to='blog/files/%Y/%m/%d/', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #author
    
    #{self.pk} : 타이틀의 앞에다가 번호를 붙여줌 프라이머리 키 의미.
    #{self.title} : 내가 설정한 타이틀로 제목을 설정해줌
    def __str__(self):
        return f'[{self.pk}]{self.title}'

    #index.html에 사용되는 함수 (블로그 링크 관력)
    def get_absolute_url(self):
        return f'/blog/{self.pk}/'  #f''는 문자열을 만드는 함수 #self.pk는 해당객체의 primary key
