"""View module for handling requests about exercises"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from fitvapi.models import Exercise


class ExerciseView(ViewSet):
    """Fit V Exercise view"""

    def retrieve(self, request, pk):
        exercise = Exercise.objects.get(pk=pk)
        serializer = ExerciseSerializer(exercise)
        return Response(serializer.data)
        

    def list(self, request):
     
        
        exercises = Exercise.objects.all()
        category = request.query_params.get('category', None)
        if category is not None:
            exercises = exercises.filter(category_id=category)
        serializer = ExerciseSerializer(exercises, many=True)
        return Response(serializer.data)
        
        
class ExerciseSerializer(serializers.ModelSerializer):
    """JSON serializer for exercises
    """
    class Meta:
        model = Exercise
        fields = ('id', 'name', 'category', 'image')
        depth = 2