from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    Authors = Author.objects.all()
    context = {
        'Authors': Authors,
    }
    return render(request, 'index.html', context)
