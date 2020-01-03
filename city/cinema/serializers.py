from rest_framework import serializers
from .models import Movie, Comment


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

    @staticmethod
    def get_movie_id(obj):
        return obj.pk

    class Meta:
        model = Movie
        fields = ('movie_id', 'total_comments', 'rank')






