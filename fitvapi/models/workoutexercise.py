from django.db import models

class WorkoutExercise(models.Model): 
    
    workout_id = models.ForeignKey("Workout", on_delete=models.CASCADE)
    exercise_id = models.ForeignKey("Exercise", on_delete=models.CASCADE)
    reps = models.IntegerField()
    sets = models.IntegerField()