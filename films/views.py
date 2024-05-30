from django.shortcuts import render
from .models import film
# Create your views here.
def home__view(request):
    filmm = film.objects.all()
    return render(request,'index.html' , {'filmm': filmm})