# tasks/models.py
from django.db import models

class Participant(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Task(models.Model):
    task_name = models.CharField(max_length=255)
    description = models.TextField()
    submission_date = models.DateField()
    participants = models.ManyToManyField(Participant, blank=True)
    

    def __str__(self):
        return self.task_name
    

