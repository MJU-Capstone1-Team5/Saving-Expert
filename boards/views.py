from django.shortcuts import render, redirect
from .models import Board, Boardcomment, Myuser, Boardcategory
from datetime import datetime



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
  if request.method == "POST":
    
    user = Myuser.objects.get(id = request.user.id)
    boardphoto = request.FILES.get("boardphto")
    boardtitle = request.POST["boardtitle"]
    boardcontext = request.POST["boardcontext"]
    postcategory = request.POST["postcategory"]
    postcategory = Boardcategory.objects.get(name = postcategory)

    now = datetime.now()
    formatted_date = now.strftime("%Y-%m-%d %H:%M")

    Board.objects.create(userid = user, title = boardtitle, context = boardcontext, category = postcategory, date = formatted_date, boardimage = boardphoto)
    
    return redirect(f"/board/{Board.objects.all().last().id}")

  category = Boardcategory.objects.all()
  context = {
    "categoryinfo": category,
  }
  return render(request, template_name="boards/create.html",context=context)