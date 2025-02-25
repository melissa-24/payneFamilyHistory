from django.shortcuts import render, redirect
from django.contrib import messages
from datetime import date 
from app.models import *

todays_date = date.today()


def index(request):
    if 'user_id' not in request.session:
        return render(request, 'index.html')
    else :
        return render(request, 'dashboard.html')
    
def timeline(request):
    return render(request, 'timeline.html')

def blanket(request):
    wedding = 1976
    current_year = todays_date.year
    years = []
    for year in range(wedding, current_year + 1):
        year = str(year)
        years.append(year)
    events = Event.objects.order_by('year').values()
    print('years',years)
    print('events',events)
    context = {
        'years': years,
        'events': events,
    }
    return render(request, '50years.html', context)
