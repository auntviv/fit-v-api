from django.db import models
from django.contrib.auth.models import User

class Workout(models.Model): 
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date = models.DateField()
    calories = models.IntegerField()


