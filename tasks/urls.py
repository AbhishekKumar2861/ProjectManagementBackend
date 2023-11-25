# tasks/urls.py
from django.urls import path
from .views import (
    ParticipantListCreateView,
    ParticipantDetailView,
    TaskListCreateView,
    TaskDetailView,
    ParticipantAdd,
    TaskDelete
)

urlpatterns = [
    # Participant URLs
    path('participants/', ParticipantListCreateView.as_view()),
    path('participants/<int:pk>/', ParticipantDetailView.as_view()),
    


    # Task URLs
    path('tasks/', TaskListCreateView.as_view()),
    path('tasks/<int:pk>/', TaskDetailView.as_view()),
    path('add-participants/',ParticipantAdd.as_view()),
    path('delete-task/', TaskDelete.as_view()),
    

]

