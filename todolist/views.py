from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime

# from todolist.forms import CreateForm

from django.contrib.auth.models import User

from todolist.models import Task
# Create your views here.

@login_required(login_url='/todolist/login/')
def show_todolist(request):
    username = request.COOKIES['username']
    user = User.objects.get(username=username)
    toDoListData = Task.objects.filter(user=user)
    context = {
        'data' : toDoListData,
        'username' : username,
        'user': user.pk
    }
    return render(request, "todolist.html", context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) 
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) 
            response.set_cookie('username', user.get_username()) 
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, "login.html", context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('username')
    return response

@login_required(login_url='/todolist/login/')
def create(request):
    if request.method == 'POST':
        username = request.COOKIES['username']
        user = User.objects.get(username=username)
        title = request.POST.get('title')
        description = request.POST.get('description')
        item = Task(user=user, title=title, description=description)
        item.save()
        return HttpResponseRedirect(reverse("todolist:show_todolist")) 
        
    context = {}
    return render(request, "create.html", context)

@login_required(login_url='/todolist/login/')
def doneTask(request, id):
    username = request.COOKIES['username']
    user = User.objects.get(username=username)
    TaskData = Task.objects.filter(user=user).get(pk=id)
    TaskData.is_finished = True
    TaskData.save()
    return HttpResponseRedirect(reverse("todolist:show_todolist")) 

@login_required(login_url='/todolist/login/')
def deleteTask(request, id):
    username = request.COOKIES['username']
    user = User.objects.get(username=username)
    TaskData = Task.objects.filter(user=user).get(pk=id)
    TaskData.delete()
    return HttpResponseRedirect(reverse("todolist:show_todolist")) 