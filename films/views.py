from django.shortcuts import render
from .models import film
# Create your views here.
def home__view(request):
    filmm = film.objects.all()
    return render(request,'index.html' , {'filmm': filmm})

def about__view(request):
    
    return render(request,'about.html' )

def contact__view(request):
    return render(request,'contact.html')