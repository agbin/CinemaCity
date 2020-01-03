from django.db import models
from django.db.models import Count, Case
from django.db.models.functions import DenseRank


class MovieManager(models.Manager):
    def counting(self, start, end):
        return super().get_queryset().annotate(
            total_comments=Count(
                models.Case(
                    models.When(comment__created__range=(start, end), then=1),
                    output_field=models.IntegerField(),
            ))).annotate(
            rank=models.Window(expression=DenseRank(), order_by=models.F('total_comments').desc())
            )


class Movie(models.Model):
    Genre = models.CharField(max_length=1000, null=True, blank=True)
    DVD = models.CharField(max_length=1000, null=True, blank=True)
    Poster = models.CharField(max_length=1000, null=True, blank=True)
    Title = models.CharField(max_length=1000, null=True, blank=True)
    BoxOffice = models.CharField(max_length=1000, null=True, blank=True)
    Production = models.CharField(max_length=1000, null=True, blank=True)
    Year = models.CharField(max_length=1000, null=True, blank=True)
    Awards = models.CharField(max_length=1000, null=True, blank=True)
    Ratings = models.CharField(max_length=1000, null=True, blank=True)
    Released = models.CharField(max_length=1000, null=True, blank=True)
    Runtime = models.CharField(max_length=1000, null=True, blank=True)
    Rated = models.CharField(max_length=1000, null=True, blank=True)
    Website = models.CharField(max_length=1000, null=True, blank=True)
    Response = models.CharField(max_length=1000, null=True, blank=True)
    imdbID = models.CharField(max_length=1000, null=True, blank=True)
    Actors = models.CharField(max_length=1000, null=True, blank=True)
    Metascore = models.CharField(max_length=1000, null=True, blank=True)
    imdbVotes = models.CharField(max_length=1000, null=True, blank=True)
    Plot = models.CharField(max_length=1000, null=True, blank=True)
    imdbRating = models.CharField(max_length=1000, null=True, blank=True)
    Writer = models.CharField(max_length=1000, null=True, blank=True)
    Director = models.CharField(max_length=1000, null=True, blank=True)
    Type = models.CharField(max_length=1000, null=True, blank=True)
    Country = models.CharField(max_length=1000, null=True, blank=True)
    Language = models.CharField(max_length=1000, null=True, blank=True)
    totalSeasons = models.CharField(max_length=1000, null=True, blank=True)

    objects = models.Manager()
    moviess = MovieManager()

    def __str__(self):
        return self.Title


class Comment(models.Model):
    comment = models.CharField(max_length=100, null=True, blank=True)
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True, blank=True)
    created = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return '{}: ({})'.format(self.movie_id, self.comment)