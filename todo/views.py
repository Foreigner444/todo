from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Task

def add_task(request):
    task = request.POST['task']
    if task:
        Task.objects.create(title=task)
    return redirect('home')
