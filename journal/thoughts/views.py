from django.shortcuts import render
from django.http import HttpResponse

from .models import Task


def home(request):
    return render(request, 'index.html')


def task(request):

    querry_all_data = Task.objects.all()

    context = {'tasks': querry_all_data}


    return render(request, 'task.html', context)
