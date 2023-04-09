from django.db import models
from django.contrib.auth.models import User

	
# Create your models here.
class Myuser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    userid = models.CharField(max_length=50, null=True, verbose_name="이름")
    password = models.CharField(max_length=50, null=True, verbose_name="비밀번호")
    nickname = models.CharField(max_length=50, null=True, verbose_name="닉네임")
    email = models.CharField(max_length=50, null=True, verbose_name="이메일")
    userimage = models.ImageField(blank=True,upload_to='userimage/',verbose_name="유저사진", null=True)
    usermemo = models.TextField(verbose_name="유저소개")