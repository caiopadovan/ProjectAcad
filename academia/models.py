from django.db import models

# Create your models here.

class MuscularGroup(models.Model):                      
    name = models.CharField(max_length=50)                    # Fields that the model needs

    def __str__(self):
        return self.name

class Exercise(models.Model):
    name = models.CharField(max_length=100)
    muscular_group = models.ForeignKey(MuscularGroup, on_delete=models.CASCADE, related_name='exercises')
    description = models.TextField()

    def __str__(self):
        return self.name

class Training(models.Model):
    name = models.CharField(max_length=50)
    exercises = models.ManyToManyField(Exercise, through='TrainingExercise', related_name='exercises_detail')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class TrainingExercise(models.Model):
    training = models.ForeignKey(Training, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    series = models.IntegerField()
    reps = models.IntegerField()
    order = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.training.name} - {self.exercise.name}"

    class Meta:
        ordering = ['order']

class TrainingExecution(models.Model):
    training = models.ForeignKey(Training, on_delete=models.CASCADE, related_name='execution')
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.training.name} - {self.date}"

class ExerciseExecution(models.Model):
    training_execution = models.ForeignKey(TrainingExecution, on_delete=models.CASCADE, related_name='exercise_execution')
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    series_done = models.IntegerField()
    reps_done = models.IntegerField()

    def __str__(self):
        return f"{self.training_execution.training} - {self.exercise.name} - {self.weight}kg"