"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from fitvapi.models import Workout


class WorkoutView(ViewSet):
    """Level up game types view"""

    def retrieve(self, request, pk):
        workout = Workout.objects.get(pk=pk)
        serializer = WorkoutSerializer(workout)
        return Response(serializer.data)
        

    def list(self, request):
       
        workouts = Workout.objects.all()
        serializer = WorkoutSerializer(workouts, many=True)
        return Response(serializer.data)
        
        
class WorkoutSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Workout
        fields = ('id', 'user', 'date', 'calories')