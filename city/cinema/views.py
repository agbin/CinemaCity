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

    
class MovieDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    lookup_field = 'Title'

    def get(self, request, Title,  *args, **kwargs):
        movie = self.kwargs['Title']
        c = movie.capitalize()
        if Movie.objects.filter(Title=c):
            b = Title.capitalize()
            queryset = Movie.objects.get(Title=b)
            serializer = self.get_serializer(queryset)
            return Response(serializer.data)
        else:
            url = 'http://www.omdbapi.com/?t=%s&apikey=279177da' % Title
            r = requests.get(url)
            dd = r.json()
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
    queryset = Movie.moviess.all()
    serializer_class = TopMoviesSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)



class TopDetail(mixins.ListModelMixin,
                generics.GenericAPIView):
    queryset = Movie.moviess.all()
    serializer_class = TopMoviesSerializer

    def get(self, request, *args, **kwargs):
        start_date = self.request.query_params.get('from_date')
        end_date = self.request.query_params.get('to_date')
        print(start_date, '-', end_date)
        return self.list(request, *args, **kwargs)


class TopMoviesViewSet(mixins.ListModelMixin,
                       viewsets.GenericViewSet):
    """
    API endpoint that allows listing top movies by comments.
    """
    serializer_class = TopMoviesSerializer

    def get_queryset(self):
        start_date = self.request.query_params.get('from_date')
        start = datetime.datetime.strptime(start_date, "%Y-%m-%d").date()
        print(start)
        print('Type: ', type(start))
        end_date = self.request.query_params.get('to_date')
        end = datetime.datetime.strptime(end_date, "%Y-%m-%d").date()
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
