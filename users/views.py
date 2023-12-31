from django.shortcuts import render, redirect

#from django.views.generic import ListView, DetailView

#from lesson_1.models import Brand, Category, Product
#from cart.forms import *
#from django.views.generic.edit import FormView
from .forms import UserRegisterForm, UserLoginForm
from django.contrib import messages
from django.contrib.auth import login, logout


menu = [
    {'title': "О нас", 'url_name': 'about'},
    {'title': "Новости", 'url_name': 'news'},
    {'title': "Условия работы", 'url_name': 'working_conditions'},
    {'title': "Отзывы", 'url_name': 'reviews'},
    {'title': "Контакты", 'url_name': 'contacts'},
    {'title': "Статьи", 'url_name': 'articles'}
]

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('users:login')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {"form": form, "menu": menu})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'users/login.html', {"form": form, "menu": menu})


def user_logout(request):
    logout(request)
    return redirect('users:login')
