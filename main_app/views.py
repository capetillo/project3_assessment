from django.shortcuts import render

# Add the following import
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Todo
# Define the home view
def home(request):
    todos = Todo.objects.all()
    return render(request, 'home.html', {'todos': todos})

class TodoCreate(CreateView):
    model = Todo
    fields = ['todo_item']
    success_url='/'

class TodoList(ListView):
    model = Todo

class TodoDetail(DetailView):
    model = Todo

class TodoUpdate(UpdateView):
    model = Todo
    fields = ['todo_item']

class TodoDelete(DeleteView):
    model = Todo
    success_url = '/'