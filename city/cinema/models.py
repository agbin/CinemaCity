from django.db import models
from django.db.models import Count, Case
from django.db.models.functions import Rank, DenseRank
from django.db.models.functions import DenseRank
from django.db.models import F, Window
from django.contrib.postgres.fields import JSONField, ArrayField
from django.core.serializers.json import DjangoJSONEncoder
import requests
from django.utils import timezone


import datetime




class MovieManager(models.Manager):

    # def counting(self, start, end):
    #     return super().get_queryset().filter().annotate(
    #         total_comments=Count('comment_set')).annotate(
    #         rank=models.Window(expression=DenseRank(), order_by=models.F('total_comments').desc())
    #         )

    # def counting(self, start, end):
    #     return super().get_queryset().filter().annotate(
    #         total_comments=models.Count('comment_set')).annotate(
    #         rank=models.Window(expression=DenseRank(), order_by=models.F('total_comments').desc())
    #         )

    # def counting(self, start, end):
    #     return super().get_queryset().annotate(
    #         total_comments=Count(
    #             models.Case(
    #                 models.When(comment__created__range=(start, end), then=1),
    #             default=0,
    #                 output_field=models.IntegerField(),
    #         ))).annotate(
    #         rank=models.Window(expression=DenseRank(), order_by=models.F('total_comments').desc())
    #         )

    def counting(self, start, end):
        return super().get_queryset().annotate(
            total_comments=Count(
                models.Case(
                    models.When(comment__created__range=(start, end), then=1),
                    output_field=models.IntegerField(),
            ))).annotate(
            rank=models.Window(expression=DenseRank(), order_by=models.F('total_comments').desc())
            )





    #
    # def allll(self, start_date, *args, **kwargs):
    #     Comment.objects.filter(start_date)
    #     return super().filter(comments__start_date__gt=start_date)

# class MovieManager(models.Manager):
#
#     # def get(self, request, year, month, day, year1, month1, day1):
#     #     start_date = datetime.date(int(year), int(month), int(day))
#     #     end_date = datetime.date(int(year1), int(month1), int(day1))
#     #     print(start_date, '-', end_date)
#     #     return self.list(request)
#
#     def counting(self, start, end):
#
#
#         # start_date = self.request.query_params.get('from_date', None)
#         #
#         # end_date = self.request.query_params.get('to_date', None)
#         return super().get_queryset().annotate(
#             total_comments=Count(models.Case(
#                     models.When(comment_set__created__range=(start, end), then=1),
#
#                     output_field=models.IntegerField(),
#             ))).annotate(
#             rank=models.Window(expression=DenseRank(), order_by=models.F('total_comments').desc())
#             )




class Movie(models.Model):
    Genre = models.CharField(max_length=1000, null=True, blank=True)
    DVD = models.CharField(max_length=1000, null=True, blank=True)
    Poster = models.CharField(max_length=1000, null=True, blank=True)
#     Title = models.CharField(max_length=1000# , null=True, blank=True)
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




    Title = models.CharField(max_length=1000, null=True, blank=True)
    totalSeasons = models.CharField(max_length=1000, null=True, blank=True)
    # created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    # last_modified = models.DateTimeField(auto_now=True, null=True, blank=True)
    # myVariable = models.CharField(null=True, max_length=100)
    # start_date = models.DateField(null=True)
    # end_date = models.DateField(null=True)
    # start = models.DateField(null=True)
    # end = models.DateField(null=True)


    objects = models.Manager()
    moviess = MovieManager()

    # class Meta:
    #     unique_together = (('id', 'Title'),)



    def totally(self):
        a = self.comment_set.all().count()
        return self.comment_set.all().count()


    def __str__(self):
        return self.Title

class CommentManager(models.Manager):

    def all(self, *args, **kwargs):
        return super().filter(movie_id=1)




class Comment(models.Model):
    comment = models.CharField(max_length=100, null=True, blank=True)
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True, blank=True)

    created = models.DateField(auto_now_add=True, null=True)
    # created = models.DateField('date', default=timezone.now(), blank=False)

    # start = models.CharField(null=True, max_length=100)
    # end = models.CharField(null=True, max_length=100)
    # last_date = models.DateTimeField('last_date', auto_now=True, null=True)

    # ?from_date = 2019 - 08 - 08 & to_date = 2019 - 12 - 06


    objects = models.Manager()
    ooo = CommentManager()



    def __str__(self):
        return '{}: ({})'.format(self.movie_id, self.comment)