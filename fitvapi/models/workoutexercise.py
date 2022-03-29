from django.db import models

class WorkoutExercise(models.Model): 
    
    workout = models.ForeignKey("Workout", on_delete=models.CASCADE)
    exercise = models.ForeignKey("Exercise", on_delete=models.CASCADE)
    reps = models.IntegerField()
    sets = models.IntegerField()