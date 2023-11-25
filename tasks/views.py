from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Participant, Task
from .serializers import ParticipantSerializer, TaskSerializer

# Participant views

class ParticipantListCreateView(APIView):
    def get(self, request):
        participants = Participant.objects.all()
        serializer = ParticipantSerializer(participants, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ParticipantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ParticipantDetailView(APIView):
    def get_object(self, pk):
        try:
            return Participant.objects.get(pk=pk)
        except Participant.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        participant = self.get_object(pk)
        serializer = ParticipantSerializer(participant)
        return Response(serializer.data)

    def put(self, request, pk):
        participant = self.get_object(pk)
        serializer = ParticipantSerializer(participant, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        participant = self.get_object(pk)
        participant.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Task views

class TaskListCreateView(APIView):
    def get(self, request):
        tasks = Task.objects.all()
        print(tasks)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        print("ta",request.data)
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskDetailView(APIView):
    def get_object(self, pk):
        try:
            return Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        task = self.get_object(pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def put(self, request, pk):
        task = self.get_object(pk)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        task = self.get_object(pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ParticipantAdd(APIView):
    def post(self, request):
        try:
            newname = request.data["name"]
            newemail = request.data["email"]
            newtask_id = request.data["task_id"]

            # Get or create the participant
            newParticipant, created = Participant.objects.get_or_create(email=newemail)
            newParticipant.name = newname
            newParticipant.save()

            # Get the task
            task = Task.objects.get(id=newtask_id)

            # Add the participant to the task
            task.participants.add(newParticipant)
            task.save()

            return Response({"message": "Participant added successfully"})

        except Exception as e:
            print(str(e))
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
class TaskDelete(APIView):
    def delete(self, request):
        try:
            task_id=request.data["task_id"]

            task = Task.objects.get(id=task_id)
            task.delete()
            return Response({"message": "Task deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Task.DoesNotExist:
            return Response({"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)

