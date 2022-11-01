from rest_framework import serializers
from .models import *

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'text stars stars_str'.split()
  
class MovieSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True)
    class Meta:
        model = Movie
        fields = 'title description rating duration reviews '.split()

class DirectorSerializer(serializers.ModelSerializer):
    movies_count = serializers.SerializerMethodField()
    class Meta:
        model = Director
        fields = 'name movies_count'.split()


    def get_movies_count(self, director):
        return director.movies.count()