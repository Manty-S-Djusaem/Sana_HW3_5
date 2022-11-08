from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import  *
from .models import Director, Movie, Review
from rest_framework import status


@api_view(['GET', 'POST'])
def director_view(request):
    if request.method == 'GET':
        directors = Director.objects.all()
        serializer = DirectorListSerializer(directors, many=True)
        return Response(data=serializer.data)
    else:
        serializers = DirectorCreateSerializer(data=request.data)
        if not serializers.is_valid():
            return Response(data={'errors': serializers.errors},
                            status=status.HTTP_406_NOT_ACCEPTABLE)
        name = request.data.get('name', '')
        print(name)
        director = Director.objects.create(
            name=name
        )
        return Response(data=DirectorSerializers(director).data)


@api_view(['GET', 'PUT', 'DELETE'])
def Director_detail_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error': 'Director not found'})
    if request.method == 'GET':
        serializers = DirectorSerializers(director)
        return Response(data=serializers.data)
    elif request.method == 'PUT':
        director.name = request.data.get('name')
        director.save()
        return Response(data=DirectorSerializers(director).data)
    else:
        director.delete()
        return Response(data={'director': 'Director removed!'},
                        status=status.HTTP_204_NO_CONTENT)







@api_view(['GET', 'POST'])
def Movie_view(request):
    if request.method == 'GET':
        movie = Movie.objects.all()
        serializer = MovieSerializers(movie, many=True)
        return Response(data=serializer.data)
    else:
        serializer = ReviewCreateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE,
                            data={'message': 'data with errors',
                                    'errors': serializer.errors})
        title = request.data.get('title' '')
        description = request.data.get('description')
        duration = request.data.get('duration')
        director_id = request.data.get('director_id')
        movie = Movie.objects.create(
            title=title, description=description, duration=duration, director_id=director_id,
        )
        movie.save()
        return Response(data=MovieSerializers(movie).data)




@api_view(['GET', 'PUT', 'DELETE'])
def Moview_detail_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'Movie': 'Movie not found'})
    if request.method == 'GET':
        serializer = MovieSerializers(movie)
        return Response(data=serializer.data)
    elif request.method == 'PUT':
        movie.title = request.data.get('title')
        movie.description = request.data.get('description')
        movie.duration = request.data.get('duration')
        movie.director_id = request.data.get('director_id')
        movie.save()
        return Response(data=MovieSerializers(movie).data)
    else:
        movie.delete()
        return Response(data={'director': 'Director removed!'},
                        status=status.HTTP_204_NO_CONTENT)




@api_view(['GET', 'POST'])
def Review_view(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(data=serializer.data)
    else:
        serializers = ReviewCreateSerializer(data=request.data)
        if not serializers.is_valid():
            return Response(data={'errors': serializers.errors},
                            status=status.HTTP_406_NOT_ACCEPTABLE)
        reviews = Review.objects.create(
            text=request.data.get('text'), stars=request.data.get('stars'), movie_id=request.data.get('movie_id')
        )
        reviews.save()
        return Response(data=ReviewSerializer(reviews).data)





@api_view(['GET', 'PUT', 'DELETE'])
def Review_detail_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'Review': 'Review not found'})
    if request.method == 'GET':
        serializers = ReviewSerializer(review)
        return Response(data=serializers.data)
    elif request.method == 'PUT':
        review.text = request.data.get('text')
        review.stars = request.data.get('stars')
        review.movie = request.data.get('movie')
        review.save()
        return Response(data=ReviewSerializer(review).data)
    else:
        review.delete()
        return Response(data={'Review': 'Review removed!'},
                              status=status.HTTP_204_NO_CONTENT)





@api_view(['GET'])
def movies_reviews_view(request):
    movies_reviews = Movie.objects.all()
    data = MoviesReviewsListSerializer(movies_reviews, many=True).data
    return Response(data=data)





