from django.shortcuts import render, redirect
from django.contrib import messages
from app.models import *


def index(request):
    if 'user_id' not in request.session:
        return render(request, 'index.html')
    else :
        return render(request, 'dashboard.html')
