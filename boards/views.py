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
    boardphoto = request.FILES.get("boardphoto")
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

def update(request,id):
  board = Board.objects.get(pk = id)
  if request.method == "POST":

    clearimage = request.POST.get('clearimage')
    boardphoto = request.FILES.get("boardphoto")
    if boardphoto == None:
      if clearimage == 'clearimage':
        boardphoto = None
      else:
        boardphoto = board.boardimage
    boardtitle = request.POST["boardtitle"]
    boardcontext = request.POST["boardcontext"]
    postcategory = request.POST["postcategory"]
    postcategory = Boardcategory.objects.get(name = postcategory)
    board.title = boardtitle
    board.context = boardcontext
    board.category = postcategory
    board.boardimage = boardphoto
    board.save()
    return redirect(f"/board/{board.id}")

  
  category = Boardcategory.objects.all()
  context = {
    "boardinfo": board,
    "categoryinfo": category,
  }
  return render(request, template_name="boards/update.html",context=context)

def delete(request, id):
  if request.method == "POST":
    Board.objects.filter(id=id).delete()
    return redirect("/board")
  
def commentcreate(request, id):
  if request.method == "POST":
    user = Myuser.objects.get(id = request.user.id)
    board = Board.objects.get(pk = id)
    commentcontext = request.POST["commentcontext"]

    now = datetime.now()
    formatted_date = now.strftime("%Y-%m-%d %H:%M")
    Boardcomment.objects.create(userid = user,boardid = board,  context = commentcontext, date = formatted_date )

    return redirect(f"/board/{id}")
  
def commentdelete(request, id,bid):
  if request.method == "POST":
    Boardcomment.objects.filter(id=id).delete()
    return redirect(f"/board/{bid}")

