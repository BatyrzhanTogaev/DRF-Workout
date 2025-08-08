from django.db import models
from django.contrib.auth.models import User


class Workout(models.Model):
    date = models.DateTimeField()
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Exercise(models.Model):
    name = models.CharField(max_length=255)
    weight = models.IntegerField()
    reps = models.IntegerField()
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
