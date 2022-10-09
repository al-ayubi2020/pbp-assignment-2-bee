from todolist.views import register
from todolist.views import login_user
from todolist.views import logout_user
from todolist.views import show_todolist
from todolist.views import create
from todolist.views import doneTask
from todolist.views import deleteTask
from todolist.views import todolist_json

from django.urls import path

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('json/', todolist_json, name='todolist_json'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create, name='create'),
    path('done/<int:id>', doneTask, name='doneTask'),
    path('delete/<int:id>', deleteTask, name='deleteTask'),
]
