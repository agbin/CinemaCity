from django.test import TestCase, Client
from django.urls import reverse, resolve
from .views import MovieList, MovieDetail
from .models import Movie, Comment
import requests
from rest_framework.response import Response


class LibraryTests(TestCase):

    # url test
    def test_url_new_movie(self):
        url = reverse('MovieList')
        # print(resolve(url))
        # self.assertEquals(resolve(url).func, MovieList)

    # views
    def test_view_MovieList(self):
        client = Client()
        response = client.get(reverse("MovieList"))
        self.assertEquals(response.status_code, 200)

    def test_view_CommentList(self):
        client = Client()
        response = client.get(reverse("CommentList"))
        self.assertEquals(response.status_code, 200)

    def test_view_TopMoviesViewSet(self):
        client = Client()
        response = client.get(reverse("TopMoviesViewSet"))
        self.assertEquals(response.status_code, 200)

    def test_adding_movie_from_omdb(self):
        url = 'http://www.omdbapi.com/?t=%s&apikey=279177da' % "Batman"
        r = requests.get(url)
        dd = r.json()
        Movie.objects.create(**dd)
        for movie in Movie.objects.values():
            print(movie)
            for field in sorted(movie):
                print(field, movie[field])
        for field1 in sorted(dd):
            print(field1, dd[field1])
        self.assertEqual(field, dd)


    #models
    def test_movie_is_not_empty(self):
        self.movie = Movie.objects.create(Title="Superman")
        self.assertEqual(str(self.movie), "Superman")

    def test_comment_is_not_empty(self):
        self.comment = Comment.objects.create(Title="Superman")
        self.assertEqual(str(self.comment), "ok")
