from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from .forms import ContactForm
# Create your views here.

def index(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # Обработка данных формы
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            subscribe = form.cleaned_data['subscribe']
            # Дальнейшая логика напрмер отправки емаил
    else:
        form = ContactForm()
    return render(request, 'index.html', {'form': form})


# def index(request):
#     if request.method == "POST":
#         # Получаем данные
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         message = request.POST.get('message')
#         subscribe = request.POST.get('subscribe') == 'on'
#
#         print(f'Name: {name}')
#         print(f'email: {email}')
#         print(f'message: {message}')
#         print(f'subscribe: {subscribe}')
#
#         # Http ответ пользователю
#         return HttpResponse('Форма успешно отправлена')
#     # Если это Get
#     return render(request, 'index.html')

# def index(request):
#     name = request.GET.get('name', 'Guest')
#     return HttpResponse(f'Hello, {name}!')

def simple_post(request):
    if request.method == "POST":
        message = request.POST.get('message', '')
        return HttpResponse(f'You said: {message}')
    return render(request, 'index2.html')

def index3(request):
    title = "Это мой сайт"
    text = 'Какой-то рандосный текст из переменной в mysite/app/views.py'
    list1 = ['aa', 'bbb', 'cccccc']
    len_list = len(list1)
    context = {
        'title': title,
        'text': text,
        'list1': list1,
        'len_list': len_list
    }
    return render(request, 'index3.html', context)

# отрабатывание ошибки
# def index(request):
#     return HttpResponse('Hello', status=400, reason='текст ошибки')


# class index2(TemplateView):
#     template_name = 'index2'











