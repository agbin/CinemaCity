from .models import Movie, Comment
from .serializers import MovieSerializer, CommentSerializer, TopMoviesSerializer
from rest_framework import mixins
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from .serializers import MovieSerializer, CommentSerializer
import requests
from rest_framework import status
from rest_framework.response import Response
import datetime
from datetime import date
from django.utils import timezone


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

    def put(self, request, *args, **kwargs):
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


class TopMoviesViewSet(mixins.ListModelMixin,
                       viewsets.GenericViewSet):
    """
    API endpoint that allows listing top movies by comments.
    """
    serializer_class = TopMoviesSerializer

    def get_queryset(self):
        start_date = self.request.query_params.get('from_date')
        if start_date:
            start = datetime.datetime.strptime(start_date, "%Y-%m-%d").date()
        end_date = self.request.query_params.get('to_date')
        if end_date:
            end = datetime.datetime.strptime(end_date, "%Y-%m-%d").date()
        if start_date and end_date:
            queryset = Movie.moviess.counting(start, end)
        else:
            queryset = Movie.moviess.counting(date(2019, 12, 12), timezone.now())
        return queryset.order_by('rank').all()


    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)








