from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import datetime

# from todolist.forms import CreateForm

from django.contrib.auth.models import User

from todolist.models import Task
# Create your views here.

@login_required(login_url='/todolist/login/')
def show_todolist(request):
    user = request.user
    toDoListData = Task.objects.filter(user=user)
    context = {
        'data' : toDoListData,
        'username' : user.username,
        'user': user.pk
    }
    return render(request, "todolist.html", context)

def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        form = UserCreationForm(request.POST)
        if username and password:
            try:
                acc = User.objects.create(username=username)
                if acc:
                    acc.set_password(password)
                    acc.save()
                    messages.success(request, 'Akun telah berhasil dibuat!')
                    return redirect('todolist:login')
                else:
                    messages.success(request, 'Terjadi masalah!')
            except:
                messages.success(request, 'Username sudah pernah digunakan!')
        else:
            messages.success(request, 'Tidak boleh kosong!')

    
    context = {}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) 
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) 
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, "login.html", context)

@login_required(login_url='/todolist/login/')
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    return response

@login_required(login_url='/todolist/login/')
def create(request):
    if request.method == 'POST':
        user = request.user
        title = request.POST.get('title')
        description = request.POST.get('description')
        item = Task(user=user, title=title, description=description)
        item.save()
        return HttpResponseRedirect(reverse("todolist:show_todolist")) 
        
    context = {}
    return render(request, "create.html", context)

@login_required(login_url='/todolist/login/')
def doneTask(request, id):
    user = request.user
    TaskData = Task.objects.filter(user=user).get(pk=id)
    TaskData.is_finished = True
    TaskData.save()
    return HttpResponseRedirect(reverse("todolist:show_todolist")) 

@login_required(login_url='/todolist/login/')
def deleteTask(request, id):
    user = request.user
    TaskData = Task.objects.filter(user=user).get(pk=id)
    TaskData.delete()
    return HttpResponseRedirect(reverse("todolist:show_todolist")) 