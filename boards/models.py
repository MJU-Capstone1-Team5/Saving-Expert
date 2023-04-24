from django.db import models
from users.models import Myuser

# Create your models here.
class Boardcategory(models.Model):
  name = models.CharField(max_length=50,verbose_name="카테고리", null=True,blank=True)

class Board(models.Model):
  userid = models.ForeignKey(Myuser,on_delete=models.CASCADE, related_name='userBoardFor')
  title = models.CharField(max_length=50,verbose_name="게시글제목", null=True,blank=True,)
  context = models.TextField(verbose_name="본문")
  category = models.ForeignKey(Boardcategory,on_delete=models.CASCADE, related_name='categoryBoardFor')
  date = models.TextField(blank=True,null=True,default="null", verbose_name="저장날짜")
  boardimage = models.ImageField(blank=True,upload_to='boardimage/',verbose_name="게시글사진", null=True)

class Boardcomment(models.Model):
  userid = models.ForeignKey(Myuser,on_delete=models.CASCADE, related_name='userCommentFor')
  boardid = models.ForeignKey(Board,on_delete=models.CASCADE, related_name='boardCommentFor')
  context = models.TextField(verbose_name="댓글내용")
  date = models.TextField(blank=True,null=True,default="null", verbose_name="저장날짜")

