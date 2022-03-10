from django.db import models
from django.contrib.auth.models import User

# Create your models here.
GENRE_CHOICES = (
    ('A','ACTION'),
    ('C','COMEDY'),
    ('R','ROMANCE'),
    ('S','SCI-FI'),
)

CATEGORY_CHOICES = (
    ('TR','TOP RATED'),
    ('MW','MOST WATCHED'),
    ('RA','RECENTLY ADDED'),
)

class Movie(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField(max_length=5000)
    image = models.ImageField(upload_to="movies")
    genre = models.CharField(choices=GENRE_CHOICES,max_length=1)
    category = models.CharField(choices=CATEGORY_CHOICES,max_length=2)
    director = models.CharField(max_length=100)
    release_date = models.DateField()
    average_rating = models.FloatField()


    def __str__(self):
        return self.name;


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(max_length=None)
    rating = models.FloatField(default=0)
    sentiment = models.CharField(max_length=20, default="None")
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username


