from rest_framework import serializers
from .models import Actor, Movie, Review


class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('title', 'overview')


class ActorListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = ('id', 'name')


class ActorSerializer(serializers.ModelSerializer):
    class MovieTitleSerializer(serializers.ModelSerializer):
      
        class Meta:
            model = Movie
            fields = ('title', )

    movie_set = MovieTitleSerializer(read_only=True, many=True)

    class Meta:
        model = Actor
        fields = ('id', 'movie_set', 'name')


class ReviewListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('title', 'content')


class MovieSerializer(serializers.ModelSerializer):
    class ActorNameSerializer(serializers.ModelSerializer):
      
        class Meta:
            model = Actor
            fields = ('name', )

    actors = ActorNameSerializer(read_only=True, many=True)
    review_set = ReviewListSerializer(read_only=True, many=True)

    class Meta:
        model = Movie
        fields = ('id', 'actors', 'review_set', 'title', 'overview', 'release_date', 'poster_path')

class ReviewSerializer(serializers.ModelSerializer):
    class MovieTitleSerializer(serializers.ModelSerializer):
    
        class Meta:
            model = Movie
            fields = ('title', )

    movie = MovieTitleSerializer(read_only=True)

    class Meta:
        model = Review
        fields = ('id', 'movie', 'title', 'content')