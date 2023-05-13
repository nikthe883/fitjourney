from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

from .forms import TaskForm

from .models import Task


def home(request):
    return render(request, 'index.html')


def task(request):

    querry_all_data = Task.objects.all()

    context = {'tasks': querry_all_data}


    return render(request, 'task.html', context)

def create_task(request):

    form = TaskForm()

    if request.method == "POST":
        
        form = TaskForm(request.POSTq)

        if form.is_valid():
            form.save()

            return redirect('task')


    context = {'form': form}
    return render(request, 'create-task.html', context)


