from django.shortcuts import render
from datetime import datetime

def index(request):
    name = 'idris'
    context = {
        'user': name,
        'now': datetime.now()
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')
