from django.db import models

class Task(models.Model):

    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    created = models.DateTimeField(auto_now=True)


class Review(models.Model):

    reviewer_name =  models.CharField(max_length= 400)

    task = models.ForeignKey(Task, on_delete=models.CASCADE)