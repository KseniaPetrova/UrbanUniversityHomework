from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator
# Create your views here.

def index(request):
    Authors = Author.objects.all()
    context = {
        'Authors': Authors,
    }
    return render(request, 'index.html', context)


#-----------------ПАГИНАЦИЯ----------------------
def ind(request):
    posts = Post.objects.all().order_by('-created_at')
    paginator = Paginator(posts, 3)  # сколько на странице влезет постов
    page_number = request.GET.get('page')  # вытаскиваем страницу на которой находится пользователь
    page_obj = paginator.get_page(page_number)  #  полкчает номер страницы
    return render(request, 'ind.html', {'page_obj': page_obj})






