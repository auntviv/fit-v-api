"""View module for handling requests about workoutExercise types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from fitvapi.models import WorkoutExercise, exercise


class WorkoutExerciseView(ViewSet):
    """Fit V Workout Log view"""

    def retrieve(self, request, pk):
        workoutExercise = WorkoutExercise.objects.get(pk=pk)
        serializer = WorkoutExerciseSerializer(workoutExercise)
        return Response(serializer.data)
        

    def update(self, request, pk):
            

        workoutExercise = WorkoutExercise.objects.get(pk=pk)
        workoutExercise.exercise=request.data["exercise"]
        workoutExercise.sets=request.data["sets"]
        workoutExercise.reps=request.data["reps"]

        workoutExercise.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def list(self, request):
       
       
        workoutExercises = WorkoutExercise.objects.all()
        workout = request.query_params.get('workout', None)
        if workout is not None:
            workoutExercises = workoutExercises.filter(workout_id=workout)
        exercise = request.query_params.get('exercise', None)
        if exercise is not None:
            workoutExercises = workoutExercises.filter(exercise_id=exercise)
        serializer = WorkoutExerciseSerializer(workoutExercises, many=True)
        return Response(serializer.data)
        
    def create(self, request):
        """Handle POST operations

        Returns
        Response -- JSON serialized workoutExercise instance
        """
        user = request.auth.user
        try:
            serializer = CreateWorkoutExerciseSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_400_BAD_REQUEST) 
    
    def destroy(self, request, pk):
        workoutExercise = WorkoutExercise.objects.get(pk=pk)
        workoutExercise.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
        
    
class WorkoutExerciseSerializer(serializers.ModelSerializer):
    """JSON serializer for workout logs
    """
    class Meta:
        model = WorkoutExercise
        fields = ('id', 'workout', 'exercise', 'reps', 'sets')
        depth = 2
        
        
class CreateWorkoutExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutExercise
        fields = [ 'exercise', 'reps', 'sets' ]