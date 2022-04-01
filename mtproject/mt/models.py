from django.db import models
from django.contrib.auth.models import AbstractUser

class 아이디(AbstractUser):
    pass



class worker(models.Model):      #tep
    이름 = models.CharField(max_length=20)
    나이 = models.IntegerField(default=0)


    def __str__(self):
        return f"{self.이름}"



class workplace(models.Model):     #temp
    작업장 = models.CharField(max_length=30)
    주소 = models.CharField(max_length=300)
    관리자 = models.CharField(max_length=20)



