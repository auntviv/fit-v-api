"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from fitvapi.models import Category


class CategoryView(ViewSet):
    """Level up game types view"""

    def retrieve(self, request, pk):
        category = Category.objects.get(pk=pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)
        
    def update(self, request, pk):
        """update"""
            
        category = Category.objects.get(pk=pk)
        category.type = request.data["type"]
        category.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def list(self, request):
       
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
        
        
class CategorySerializer(serializers.ModelSerializer):
    """JSON serializer for category types
    """
    class Meta:
        model = Category
        fields = ('id', 'type')
        depth = 2