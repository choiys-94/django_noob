from django.shortcuts import render

from home.models import Users, Board

def index(request):
    return render(request, 'home/index.html')

def ViewBoard(request):
    return render(request, 'home/viewboard.html')