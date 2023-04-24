from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

	
# Create your models here.
class Myuser(AbstractUser,models.Model):
    email = models.CharField(max_length=50, null=True, verbose_name="이메일")
    userimage = models.ImageField(blank=True,upload_to='userimage/',verbose_name="유저사진", null=True)
    usermemo = models.TextField(verbose_name="유저소개")