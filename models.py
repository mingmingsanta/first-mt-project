from django.db import models
from django.contrib.auth.models import AbstractUser

class 아이디(AbstractUser):
   pass


class workplace(models.Model):     #temp
    작업장 = models.Field(max_length=300)
    주소 = models.CharField(max_length=300)
    관리자 = models.CharField(max_length=20)


    def __str__(self):
        return self.작업장





class worker(models.Model):      #tep
    이름 = models.CharField(max_length=20)
    나이 = models.IntegerField(default=0)
    작업장1 = models.ForeignKey(workplace, on_delete=models.CASCADE)
    체온 = models.IntegerField(default=0)
    비상버튼 = models.CharField(max_length=20)


    def __str__(self):
        return self.이름






