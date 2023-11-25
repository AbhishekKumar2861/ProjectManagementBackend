# tasks/admin.py
from django.contrib import admin
from .models import Task, Participant

admin.site.register(Task)
admin.site.register(Participant)
