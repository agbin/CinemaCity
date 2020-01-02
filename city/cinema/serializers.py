from rest_framework import serializers
from rest_framework.serializers import SerializerMethodField
from .models import Movie, Comment
from django.db.models.functions import DenseRank
import datetime


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['movie_id', 'comment']


class MovieSerializer(serializers.ModelSerializer):
    comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)


    def get_total_comments(self, obj):
        return obj.comment_set.count()

    class Meta:
        model = Movie
        fields = '__all__'









class TopMoviesSerializer(serializers.ModelSerializer):
    total_comments = serializers.IntegerField(read_only=True)
    rank = serializers.IntegerField(read_only=True)
    movie_id = serializers.SerializerMethodField(read_only=True)
    # comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # totally = serializers.SerializerMethodField()
    # start = serializers.SerializerMethodField()
    # end = serializers.SerializerMethodField()

    # def get_start(self, obj):
    #     value = self.context['request'].query_params.get('start')
    #     # value = datetime.datetime.strptime(value, "%Y-%m-%d").date()
    #     # comment_obj = Comment(
    #     #     start=value,
    #     # )
    #     # comment_obj.save()
    #     return value
    #
    #
    #
    #
    # def get_end(self, obj):
    #     value = self.context['request'].query_params.get('end')
    #     # value = datetime.datetime.strptime(value, "%Y-%m-%d").date()
    #     # comment_obj = Comment(
    #     #     end=value,
    #     # )
    #     # comment_obj.save()
    #     return value





    # def get_total_comments(self, obj):
    #     return obj.comment_set.count()


    # def get_totally(self, obj):
    #     return obj.totally()




    @staticmethod
    def get_movie_id(obj):
        return obj.pk

    class Meta:
        model = Movie
        fields = ('movie_id', 'total_comments', 'rank')






