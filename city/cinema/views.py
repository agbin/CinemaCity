from .models import Movie, Comment
from .serializers import MovieSerializer, CommentSerializer, TopMoviesSerializer
from rest_framework import mixins
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models.functions import Lower
from rest_framework.filters import OrderingFilter
from django.db.models import Count
from rest_framework import viewsets
import django_filters.rest_framework
import requests
from .serializers import MovieSerializer, CommentSerializer
from .models import Movie, Comment
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from rest_framework.response import Response

from rest_framework.parsers import JSONParser
import requests

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer

import urllib.parse
from urllib.parse import urlencode

from django.http import HttpResponse

from rest_framework.decorators import api_view, permission_classes
# from .permissions import Check_API_KEY_Auth

from django.shortcuts import redirect
from django.http import Http404
import json
from rest_framework.response import Response
import io
import datetime
from datetime import date



class MovieList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id']
    lookup_field = 'slug'

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    # def post(self, request, format=None):
    #
    #     if request.data.get("Title"):
    #         Title = request.data["Title"]
    #         print(Title)
    #         if Movie.objects.filter(Title=Title):
    #             # return self.get(request)
    #
    #             movie_in_db = Movie.objects.get(Title=Title)
    #             serializer = self.get_serializer(movie_in_db)
    #             return Response(serializer.data)
    #
    #             # Movie.objects.get(Title=Title)
    #
    #             # serializer = self.get_serializer(request)
    #             # return Response(serializer.data)
    #
    #         else:
    #             url = 'http://www.omdbapi.com/?t=%s&apikey=279177da' % Title
    #
    #             r = requests.get(url)
    #             print(r)
    #             dd = r.json()
    #
    #             print(dd)
    #
    #         content = Movie.objects.create(**dd)
    #         serializer = self.get_serializer(content)
    #         return Response(serializer.data)
        # if request.method == "POST":
        #     if request.data.post(dd):
        #
        #         data = json.dumps(dd)
        #         serializer = MovieSerializer(data=request.data)
        #         if serializer.is_valid():
        #             serializer.save()
        #             return Response(serializer.data, status=status.HTTP_201_CREATED)
        #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# class MovieList(generics.ListAPIView):
#     serializer_class = MovieSerializer
#
#     def get_queryset(self):
#         """
#         Optionally restricts the returned purchases to a given user,
#         by filtering against a `username` query parameter in the URL.
#         """
#         queryset = Movie.objects.all()
#         movie = self.request.query_params.get('Title', None)
#         print(movie)
#         if movie is not None:
#             queryset = queryset.filter(movie__title='Title')
#             # queryset = Movie.objects.get(Title='Title')
#             serializer = self.get_serializer(queryset)
#             return Response(serializer.data)
#         else:
#             url = 'http://www.omdbapi.com/?t=%s&apikey=279177da' % movie
#
#             r = requests.get(url)
#             # print(r)
#             dd = r.json()
#
#             # print(dd)
#
#             content = Movie.objects.create(**dd)
#             serializer = self.get_serializer(content)
#             # return Response(serializer.data)
#
#             # queryset = queryset.filter(purchaser__username=username)
#         return queryset



class MovieDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    lookup_field = 'Title'


    #
    # def get(self, request, Title):
    #
    #     url = 'http://www.omdbapi.com/?t=%s&apikey=279177da' % Title
    #     r = requests.get(url)
    #     data = r.json()
    #     return Response(data, status=status.HTTP_200_OK)

    def get(self, request, Title,  *args, **kwargs):
        print('1ooooooooooooooooooooooooooooooooooooooooooooo')

        # if request.args.get('Title', ''):
        # if start_date = self.request.query_params.get('from_date')


        movie = self.kwargs['Title']



        print(movie)
        c = movie.capitalize()
        print(c)
        print(Title)
        # request.data.get('Title')
        # print('2ooooooooooooooooooooooooooooooooooooooooooooo')

        # Title = request.data['Title']
        # print('3ooooooooooooooooooooooooooooooooooooooooooooo')

        # movie = self.request.query_params.get('Title', None)
        # print(movie)
        # if movie is not None:
        # a = Movie.objects.get(movie__title=Title)
        # if a:
        # if Movie.objects.filter(Title__icontains=movie):


        # for i in Movie.objects.Title():
        #     print(i)

        if Movie.objects.filter(Title=c):


        # a = Movie.objects.filter(Title__icontains=movie)
        # if a:
            print('4ooooooooooooooooooooooooooooooooooooooooooooo')

            # return self.get(request)
            b = Title.capitalize()
            queryset = Movie.objects.get(Title=b)
            serializer = self.get_serializer(queryset)
            return Response(serializer.data)
        else:
            print('5ooooooooooooooooooooooooooooooooooooooooooooo')


            url = 'http://www.omdbapi.com/?t=%s&apikey=279177da' % Title

            r = requests.get(url)
            # print(r)
            dd = r.json()

            # print(dd)

            content = Movie.objects.create(**dd)
            serializer = self.get_serializer(content)
            return Response(serializer.data)




    def put(self, request, Title, *args, **kwargs):
        # json.loads('movie')

        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class CommentList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CommentDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer



    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class TopList(mixins.ListModelMixin,
                generics.GenericAPIView):
    # queryset = Comment.objects.all()
    queryset = Movie.moviess.all()
    # queryset = Comment.objects.top_movies_ids()
    serializer_class = TopMoviesSerializer
    # filter_backends = (DjangoFilterBackend, OrderingFilter,)
    # # filter_backends = ('django_filters.rest_framework.DjangoFilterBackend')
    # ordering = ('-id')
    # lookup_field = ('start_date', 'last_date')

    def get(self, request, *args, **kwargs):



        # from_date_param = self.request.query_params.get('from_date')
        # to_date_param = self.request.query_params.get('to_date')
        #
        # from_date = date.fromisoformat(from_date_param)
        # to_date = date.fromisoformat(to_date_param)
        #
        #
        # queryset = Movie.objects.comments_ranking(from_date, to_date)
        #
        # return queryset.order_by('rank').all()
        return self.list(request, *args, **kwargs)



class TopDetail(mixins.ListModelMixin,
                generics.GenericAPIView):
    queryset = Movie.moviess.all()
    serializer_class = TopMoviesSerializer


    # def get(self, request, *args, **kwargs):
    #
    #     return self.list(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
    # def get_queryset(self):


        start_date = self.request.query_params.get('from_date')
        # start_date = self.context['request'].query_params.get('from_date')
        # start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d").date()
        end_date = self.request.query_params.get('to_date')
        # end_date = self.context['request'].query_params.get('to_date')
        # end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d").date()
        # date_from = datetime.datetime.strptime(request.GET['q1'], '%Y-%m-%d')
        # date_to = datetime.datetime.strptime(request.GET['q2'], '%Y-%m-%d')

        print(start_date, '-', end_date)

        # return self.list(request, *args, **kwargs)
        # return self.list(request, *args, **kwargs)

        # queryset = Movie.objects.counting(start_date, end_date)

        # return queryset.all()

        return self.list(request, *args, **kwargs)

    # def get(self, request, year, month, day, year1, month1, day1):
    #     start_date = datetime.date(int(year), int(month), int(day))
    #     end_date = datetime.date(int(year1), int(month1), int(day1))
    #     print(start_date, '-', end_date)
    #     return self.list(request)

class TopMoviesViewSet(mixins.ListModelMixin,
                       viewsets.GenericViewSet):
    """
    API endpoint that allows listing top movies by comments.
    """
    serializer_class = TopMoviesSerializer
    # queryset = Movie.moviess.all()

    def get_queryset(self):
        # start = datetime.datetime.strptime(self.request.query_params.get('from_date'), '%Y-%m-%d').strftime('%Y-%m-%d')
        # print(start)
        # print('Type: ', type(start))
        # end = datetime.datetime.strptime(self.request.query_params.get('to_date'), '%Y-%m-%d').strftime('%Y-%m-%d')


        start_date = self.request.query_params.get('from_date')
        # start_date = self.context['request'].query_params.get('from_date')
        start = datetime.datetime.strptime(start_date, "%Y-%m-%d").date()

        print(start)
        print('Type: ', type(start))

        end_date = self.request.query_params.get('to_date')
        # end_date = self.context['request'].query_params.get('to_date')
        end = datetime.datetime.strptime(end_date, "%Y-%m-%d").date()

        # start= date(2011, 5, 3)
        # end = date(2011, 5, 10)

        # ff = Comment.objects.all()
        # ff.filter(created=2019-12-17)
        # print(ff)

        print(start, end)
        min = start - end
        print(min)

        queryset = Movie.moviess.counting(start, end)

        return queryset.order_by('rank').all()


    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())


        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)















import datetime

def day_archive(request, year, month, day):
    # date_year = self.cleaned_data.get("year")
    # date_month = self.cleaned_data.get("month")
    # date_day = self.cleaned_data.get("day")
    # year = self.request.query_params.get('from_date', None)
    # start_date = self.request.query_params.get('from_date', None)
    # start_date = self.request.query_params.get('from_date', None)
    date = datetime.date(int(year), int(month), int(day))
    print(date)
    return date