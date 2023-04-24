from django.shortcuts import render
from .models import Board, Boardcomment

# Create your views here.

def board(request):
  allboard = Board.objects.all()
  
  context = {
    "boardinfo": allboard,
  }
  return render(request, template_name='boards/home.html',context=context)

def detail(request,id):
  board = Board.objects.get(id = id)
  comment = Boardcomment.objects.filter(boardid = board)

  context = {
    "boardinfo": board,
    "commentinfo": comment,
  }
  return render(request, template_name ='boards/detail.html',context=context)

def create(request):
  