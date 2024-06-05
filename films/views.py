from django.shortcuts import render, redirect,get_object_or_404
from django.urls import reverse
from .models import film, Comment
from .forms import filmForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def home__view(request):
    return render(request,'index.html' )

@login_required(login_url="account:login")
def filmm__view(request):
    keyword = request.GET.get("keyword")
    if keyword:
        filmm = film.objects.filter(title__contains=keyword)
        return render(request, "filmm.html", {"filmm": filmm})
    
    
    filmm = film.objects.all()
    return render(request,'filmm.html' , {'filmm': filmm})

@login_required(login_url="account:login")
def addfilms__view(request):
    form = filmForm(request.POST or None,request.FILES or None )
    if form.is_valid():
        film = form.save(commit=False)
        film.author = request.user
        film.save()  
        messages.success(request, "Məqaləniz uğurla əlavə olundu...")
        return redirect("dashboard")
         
         
    context = {"form" : form}
    return render(request,'addfilms.html', context)

@login_required(login_url="account:login")
def films__update__view(request, id):
    films = get_object_or_404(film, id = id)
    form = filmForm(request.POST or None,request.FILES or None , instance=films)
    if form.is_valid():
        film = form.save(commit=False)
        film.author = request.user
        film.save()  
        messages.success(request, "Məqaləniz uğurla update olundu...")
        return redirect("dashboard")
         
    context = {"form" : form}
    return render(request,'update.html', context)

@login_required(login_url="account:login")
def films__delete__view(request, id):
    films = get_object_or_404(film, id=id)
    films.delete()
    messages.success(request, "Məqaləniz uğurla silindi...")
    return redirect("dashboard")

@login_required(login_url="account:login")
def dashboard__view(request):
    filmm = film.objects.filter(author = request.user)
    return render(request,'dashboard.html' , {'filmm': filmm})

@login_required(login_url="account:login")
def films__detail__view(request, id):
    # films = film.objects.filter(id = id).first()/
    # context = {"film" : film}
    films = get_object_or_404(film, id = id)
    comments = Comment.objects.filter(films = films)
    
     context = {
        "film": film,
        "comments": comments,
    }
     
    return render(request,'films-detail.html' ,context)

def about__view(request):
    
    return render(request,'about.html' )

def contact__view(request):
    return render(request,'contact.html')