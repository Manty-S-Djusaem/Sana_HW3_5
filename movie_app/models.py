from django.db import models
from django.db.models import Avg

class Director(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.name

    

class Movie(models.Model):
    title = models.CharField(max_length=25)
    description = models.TextField(max_length=100, null=True, blank=not False)
    duration = models.IntegerField(null=True)
    director = models.ForeignKey(Director, on_delete=models.CASCADE, null=True, related_name='movies') 

    def __str__(self) -> str:
        return self.title
    
    @property
    def rating(self):
        avg_rating = self.reviews.aggregate(avg_rating=Avg('stars'))['avg_rating']
        return avg_rating
    

STARS = (
    (1, '*'),
    (2, '**' ),
    (3, '***'),
    (4, '****'),
    (5, '*****')
)
    
class Review(models.Model):
    text = models.TextField(max_length=150, null=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, blank=True, null=True, related_name='reviews')
    stars = models.IntegerField(default=3, choices=STARS)

    def __str__(self) -> str:
        return self.text

    def stars_str(self):
        return self.stars * '* '