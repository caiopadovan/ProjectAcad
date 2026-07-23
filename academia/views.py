from django.shortcuts import render
from rest_framework import viewsets
from .models import MuscularGroup, Exercise, Training, TrainingExercise, TrainingExecution, ExerciseExecution
from .serializers import MuscularGroupSerializer, ExerciseSerializer, TrainingSerializer, TrainingExerciseSerializer, TrainingExecutionSerializer, ExerciseExecutionSerializer

# Create your views here.

class MuscularGroupViewSet(viewsets.ModelViewSet):                   # ModelViewSet - class that already has CRUD methods
    queryset = MuscularGroup.objects.all()                           # Setting this view to see all the data in MuscularGroup
    serializer_class = MuscularGroupSerializer                       # Which serializer class will use

class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer

class TrainingViewSet(viewsets.ModelViewSet):
    queryset = Training.objects.all()
    serializer_class = TrainingSerializer

class TrainingExerciseViewSet(viewsets.ModelViewSet):
    queryset = TrainingExercise.objects.all()
    serializer_class = TrainingExerciseSerializer

class TrainingExecutionViewSet(viewsets.ModelViewSet):
    queryset = TrainingExecution.objects.all()
    serializer_class = TrainingExecutionSerializer

class ExerciseExecutionViewSet(viewsets.ModelViewSet):
    queryset = ExerciseExecution.objects.all()
    serializer_class = ExerciseExecutionSerializer