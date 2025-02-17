from django.shortcuts import render
from .models import Game

def product_page(request):
    games = Game.objects.all()
    return render(request, 'product.html',{'games': games})

def home_page(request):
    games = Game.objects.all()
    return render(request, 'index.html',{'games': games})

# Create your views here.


def about_page(request):
    return render(request, 'about.html')

def contact_page(request):
    return render(request, 'contact.html')

def remot_page(request):
    return render(request, 'remot.html')

def video_page(request):
    return render(request, 'video.html')
