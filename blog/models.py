from django.db import models

# Create your models here.
class Post(models.Model): #일종의 db구조 , field설정
    title = models.CharField(max_length=30)
    contents = models.TextField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #author
    
    #{self.pk} : 타이틀의 앞에다가 번호를 붙여줌.
    #{self.title} : 내가 설정한 타이틀로 제목을 설정해줌
    def __str__(self):
        return f'[{self.pk}]{self.title}'
    