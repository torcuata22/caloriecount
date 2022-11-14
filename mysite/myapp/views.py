from django.shortcuts import render
from django.db import models
# Create your views here.
class Food(models.Model):
    name = models.CharField(max_length=100)
    carbs = models.FloatField()
    protein = models.FloatField()
    fats = models.FloatField()
    calories=models.IntegerField()
