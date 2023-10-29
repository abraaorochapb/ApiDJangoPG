from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework.views import APIView  
from rest_framework.response import Response
from rest_framework import status

class AnimesViewSet(APIView):  
    def get(self, request, id=None):  
        if id:
            anime = get_object_or_404(models.Animes, id=id)  
            serializer = serializers.AnimesSerializer(anime)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        
        animes = models.Animes.objects.all()
        serializer = serializers.AnimesSerializer(animes, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = serializers.AnimesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id=None):
        anime = get_object_or_404(models.Animes, id=id)
        serializer = serializers.AnimesSerializer(anime, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id=None):
        anime = get_object_or_404(models.Animes, id=id)
        anime.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)