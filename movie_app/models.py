from django.db import models

# Create your models here.
class Director(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=False)
    duration = models.IntegerField(null=True)
    director = models.ForeignKey(Director, on_delete=models.CASCADE, null=False, related_name='movies')

    def __str__(self):
        return self.title

    @property
    def filter_reviews(self):
        return self.reviews.filter(stars__in=[4, 5])


    @property
    def rating(self):
        reviews = self.filter_reviews
        count = reviews.count()
        sum_ = 0
        for i in reviews:
            sum_ += i.stars
        try:
            return sum_ / count
        except ZeroDivisionError:
            return 0

STARS = (
    (1, '*'),
    (2, '* *'),
    (3, '* * *'),
    (4, '* * * *'),
    (5, '* * * * *')
)


class Review(models.Model):
    text = models.CharField(max_length=100, null=True)
    stars = models.IntegerField(max_length=1, choices=[(int(i), i) for i in range(0, 5)],
                             default='5')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.text

    def stars_str(self):
        return int(self.stars) * '*'

    @property
    def movie_name(self):
        return self.movie.title