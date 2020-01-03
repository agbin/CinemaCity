from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import MovieList, MovieDetail, CommentList, CommentDetail, TopMoviesViewSet



urlpatterns = [
    path('movies/', MovieList.as_view()),
    path('movies/<slug:Title>/', MovieDetail.as_view()),
    path('comments/', CommentList.as_view()),
    path('comments/<int:pk>/', CommentDetail.as_view()),
    path('top/', TopMoviesViewSet.as_view({'get': 'list'})),
]

urlpatterns = format_suffix_patterns(urlpatterns)