from django.shortcuts import render

# Create your views here.
from studybug.models import Room


def home(request):
    rooms = Room.objects.all()
    return render(request,'home.html',{'rooms':rooms})

# def home(request):
#     rooms = Room.objects.all()
#     return render(request,'home.html',{'room':rooms})