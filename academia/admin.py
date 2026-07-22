from django.contrib import admin
from .models import MuscularGroup, Exercise, Training, TrainingExercise, TrainingExecution, ExerciseExecution
# Register your models here.

admin.site.register(MuscularGroup)
admin.site.register(Exercise)
admin.site.register(Training)
admin.site.register(TrainingExercise)
admin.site.register(TrainingExecution)
admin.site.register(ExerciseExecution)