from rest_framework import serializers
from .models import Artist, Music

class ArtistListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Artist
        fields = ('id', 'name')

class ArtistSerializer(serializers.ModelSerializer):
    class MusicSerializer(serializers.ModelSerializer):
      
        class Meta:
            model = Music
            fields = ('title',)

    music_set = MusicSerializer(read_only=True, many=True)
    music_count = serializers.IntegerField(
        source = 'music_set.count',
        read_only=True,
    )

    class Meta:
        model = Artist
        fields = ('id', 'name', 'music_set', 'music_count')
        # depth = 1       # depth로 관계되어있는 친구들 불러올 수 있음! (default = 0)

class MusicListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Music
        fields = ('id', 'title')


class MusicSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer(read_only=True)

    class Meta:
        model = Music
        fields = ('id', 'title', 'artist')