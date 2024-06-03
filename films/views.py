from django.shortcuts import render
from .models import film
# Create your views here.
def home__view(request):
    return render(request,'index.html' )

def our__blogs__view(request):
    filmm = film.objects.all()
    return render(request,'our-blogs.html' , {'filmm': filmm})

def my__blogs__view(request):
    filmm = film.objects.all()
    return render(request,'my-blogs.html' , {'filmm': filmm})

def about__view(request):
    
    return render(request,'about.html' )

def contact__view(request):
    return render(request,'contact.html')