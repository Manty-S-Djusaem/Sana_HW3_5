from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ReviewSerializer, DirectorSerializer, MovieSerializer
from .models import Director, Movie, Review
from rest_framework import status

'''---------------------------Director all methods--------------------------'''
@api_view(['GET', "POST"])
def directors_view(request):
    if request.method == "GET":
        directors = Director.objects.all()
        serializer = DirectorSerializer(directors, many=True)
        return Response(data=serializer.data)
    else:
        director = Director.objects.create(
            name=request.data.get('name', '')
        )
        return Response(data=DirectorSerializer(director).data)
        


@api_view(['GET', "PUT", "DELETE"])
def director_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(status=404)
    if request.method == "GET":
        serializer = DirectorSerializer(director)
        return Response(data=serializer.data)
    elif request.method == 'PUT':
        director.name = request.data.get('name', "")
        director.movies_count = request.data.get('movies_count', 0)
        director.save()
        return Response(data=DirectorSerializer(director).data)
    else:
        director.delete()
        return Response(data={'successfully remove': 'director'},status=status.HTTP_204_NO_CONTENT)


'''---------------------------Movie all methods'-----------------------------'''


@api_view(['GET', 'POST'])
def movies_view(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=not False)
        return Response(data=serializer.data)
    else:
        title = request.data.get('title', '')
        description = request.data.get('description', '')
        duration = request.data.get('duration', 0)
        director_id = request.data.get('director_id')
        movies = Movie.objects.create(
            title=title,
            description=description,
            duration=duration,
            director_id=director_id
        )
        return Response(data=MovieSerializer(movies).data)





@api_view(['GET', 'PUT', 'DELETE'])
def movie_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(data={'movie: not found'})
    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(data=serializer.data)
    elif request.method == 'PUT':
        movie.title = request.data.get('title', '')
        movie.description = request.data.get('description', '')
        movie.duration = request.data.get('duration', 0)
        movie.director = request.data.get('director_id')
        return Response(data=MovieSerializer(movie).data)
    else:
        movie.delete()
        return Response(data={'successfully remove': 'movie'},status=status.HTTP_204_NO_CONTENT)


'''------------------------------Reviews all methods--------------------------'''


@api_view(['GET', "POST"])
def reviews_view(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(data=serializer.data)
    else:
        text = request.data.get('text', "")
        stars = request.data.get('stars', 2)
        review = Review()
        review.text = text
        review.stars = stars
        review.save()
        return Response(data=ReviewSerializer(review).data)
        




@api_view(['GET', 'PUT', 'DELETE'])
def review_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist():
        return Response(data={'review': 'not found'})
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(data=serializer.data)
    elif request.method == 'DELETE':
        review.delete()
        return Response(data={'successfully remove': 'review'},status=status.HTTP_204_NO_CONTENT)
    else:
        text = request.data.get('text', "")
        stars = request.data.get('stars', 2)
        review.text = text
        review.stars = stars
        review.save()
        return Response(data=ReviewSerializer(review).data)


