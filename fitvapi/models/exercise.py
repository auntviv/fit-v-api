from django.db import models

class Exercise(models.Model): 
    
    name = models.CharField(max_length=50)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    image = models.URLField()