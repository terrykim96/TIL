from rest_framework import serializers
from .models import Article, Comment

class ArticleListSerializer(serializers.ModelSerializer):
    num_of_comment = serializers.IntegerField(
        source = 'comment_set.count',
        read_only=True,
    )
    
    class Meta:
        model = Article
        fields = ('pk', 'title', 'num_of_comment', 'content', 'created_at', 'updated_at')


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('title', 'content', 'created_at', 'updated_at')

class CommentListSerializer(serializers.ModelSerializer):
    article = ArticleSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ('pk', 'content', 'article', 'created_at', 'updated_at')


class CommentSerializer(serializers.ModelSerializer):
    article = ArticleSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ('pk', 'content', 'article', 'created_at', 'updated_at')