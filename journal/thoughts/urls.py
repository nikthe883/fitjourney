from . import views
from django.urls import path



urlpatterns = [
    path('',views.home, name='home'),

    path('task', views.task, name='task'),

    path('create-task', views.create_task, name='create-task')
]
