from django.contrib import messages
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponse
from django import forms
from requests import request

from .models import Todo
from todos.forms import TodoForm


def index(request):
    """
    return HttpResponse('Hello world')
    """
    todos = Todo.objects.all()[:10]
    context = {
        'todos': todos
    }
    return render(request, 'index.html', context)


def details(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    context = {
        'todo': todo
    }
    return render(request, 'details.html', context)


def add(request):
    if request.method == 'POST':
        title = request.POST['title']
        text = request.POST['text']

        todo = Todo(title=title, text=text)
        todo.save()

        return redirect('/todos')
    else:
        return render(request, 'add.html')


class TodoUpdate(UpdateView):
    model = Todo
    #fields = ['title', 'text']
    template_name = "todo_update_form.html"
    name = "update"
    form_class = TodoForm

    def get_success_url(self):
        return reverse('index')


class TodoDelete(DeleteView):
    model = Todo
    template_name = 'todo_confirm_delete.html'

    def get_success_url(self):
        return reverse('index')
    success_url = reverse_lazy('todos:index')