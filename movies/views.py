from django.shortcuts import render
from .models import Movie
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import MovieSerializer

# Create your views here.
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [permissions.AllowAny]