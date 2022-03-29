from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from fitvapi.models import exercise, workout, workoutexercise
from fitvapi.views import register_user, login_user 
from rest_framework import routers
from fitvapi.views import ExerciseView
from fitvapi.views import WorkoutView
from fitvapi.views import CategoryView
from fitvapi.views import WorkoutExerciseView


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'exercises', ExerciseView, 'exercise')
router.register(r'workouts', WorkoutView, 'workout')
router.register(r'categories', CategoryView, 'category')
router.register(r'workoutExercises',WorkoutExerciseView , 'workoutexercise')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register', register_user),
    path('login', login_user),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
    path('', include(router.urls))
]
