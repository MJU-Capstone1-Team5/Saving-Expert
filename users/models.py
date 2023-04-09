from django.db import models

# Create your models here.
class User(models.Model):
    userid = models.CharField(max_length=50, null=True, verbose_name="이름")
    password = models.CharField(max_length=50, null=True, verbose_name="비밀번호")
    nickname = models.CharField(max_length=50, null=True, verbose_name="비밀번호")
    email = models.CharField(max_length=50, null=True, verbose_name="비밀번호")
    userimage = models.ImageField(blank=True,upload_to='userimage/',verbose_name="유저사진", null=True)
    usermemo = models.TextField(verbose_name="유저소개")