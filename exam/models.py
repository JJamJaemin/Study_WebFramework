from django.db import models


# Create your models here.
class Student(models.Model):  # 일종의 db구조 , field설정
    num = models.CharField(max_length=15)
    name = models.CharField(max_length=30)
    birth = models.DateField()
    Depart = models.CharField(max_length=100)

    image = models.ImageField(upload_to='exam/images/%y%m%d/', blank=True)
    # author
    def get_absolute_url(self):
        return f'/exam/prob/{self.pk}/'

    def __str__(self):
        return f'[{self.num}]{self.name}'


