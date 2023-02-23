from .models import Movie
from django.contrib.auth.models import User, Group
from rest_framework import serializers

class MovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movie
        fields = ['movieName', 'genre', 'rating', 'poster']