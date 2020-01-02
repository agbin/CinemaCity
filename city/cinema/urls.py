from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import MovieList, MovieDetail, CommentList, CommentDetail, TopList, TopDetail, day_archive, TopMoviesViewSet



urlpatterns = [
    # path('movies2/', MovieList.as_view()),
    path('movies/', MovieList.as_view()),
    path('movies/<slug:Title>/', MovieDetail.as_view()),
    # url('^movies/(?P<Title>.+)/$', MovieDetail.as_view()),
    path('comments/', CommentList.as_view()),
    path('comments/<int:pk>/', CommentDetail.as_view()),
    path('top/', TopList.as_view()),
    path('top1/', TopDetail.as_view()),
    path('top3/', TopMoviesViewSet.as_view({'get': 'list'})),
    # url(r'top1/(\d{4})/(\d{2})/(\d{2})/(\d{4})/(\d{2})/(\d{2})/$', TopDetail.as_view()),
    # path('top1/', TopDetail.as_view()),
    # url(r'top1/', MyViewset.as_view()),
    # path('top1/<int:year>/<int:month>/', TopDetail.as_view()),
    # url(r'^top1/(?P<date>\d{4}-\d{2}-\d{2})/$', TopDetail.as_view()),
    # url(r'^top1/?start_date=(?P<start_date>\d{2}-\d{2}-\d{4})/?offset(?P<date_offset>\d{2}-\d{2}-\d{4})/$', TopDetail.as_view()),
    url(r'^top2/(\d{4})/(\d{2})/(\d{2})/$', day_archive),
]

urlpatterns = format_suffix_patterns(urlpatterns)