from rest_framework import serializers
from .models import MuscularGroup, Exercise, Training, TrainingExercise, TrainingExecution, ExerciseExecution


class MuscularGroupSerializer(serializers.ModelSerializer):       # Serializer = the bridget between Python and JSON, can do GET and POST methods
    class Meta:                                                   
        model = MuscularGroup                                     # Which model this serializer represents
        fields = '__all__'                                        # Which fields will be used


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'


class TrainingExerciseSerializer(serializers.ModelSerializer):
    exercise = ExerciseSerializer(read_only=True)

    class Meta:
        model = TrainingExercise
        fields = ['id', 'exercise', 'series', 'reps', 'order']


class TrainingSerializer(serializers.ModelSerializer):
    exercises_detail = TrainingExerciseSerializer(many=True, read_only=True)

    class Meta:
        model = Training
        fields = ['id', 'name', 'created', 'exercises_detail']


class ExerciseExecutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseExecution
        fields = '__all__'


class TrainingExecutionSerializer(serializers.ModelSerializer):
    exercise_execution = ExerciseExecutionSerializer(many=True, read_only=True)

    class Meta:
        model = TrainingExecution
        fields = ['id', 'training', 'date', 'exercise_execution']