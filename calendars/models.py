from django.db import models
from users.models import Myuser


# Create your models here.


class Budgetcategory(models.Model):
  name = models.CharField(max_length=50,verbose_name="카테고리", null=True,blank=True)

class Budget(models.Model):
  userid = models.ForeignKey(Myuser,on_delete=models.CASCADE, related_name='userBugetFor')
  title = models.CharField(max_length=50,verbose_name="수입지출제목", null=True,blank=True,)
  kind = models.BooleanField(default=True, verbose_name='종류') #True = 수입 False = 지출
  amount = models.IntegerField(blank=True,null=True,default=0,verbose_name="액수")
  memo = models.TextField(verbose_name="수입지출메모")
  category = models.ForeignKey(Budgetcategory,on_delete=models.CASCADE, related_name='categorybudgetfor')
  date = models.TextField(blank=True,null=True,default="null", verbose_name="저장날짜")

  