from django.test import TestCase
from django.urls import reverse, resolve
from .views import MovieList

class BibliotekaTests(TestCase):

    # url test
    def test_url_new_movie(self):
        url = reverse('MovieList')
        print(url)
