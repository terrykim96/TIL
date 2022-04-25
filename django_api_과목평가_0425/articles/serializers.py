from rest_framework import serializers
from .models import Article, Comment


class ArticleListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('id', 'title', 'content')


class CommentSerializer(serializers.ModelSerializer):
    # Q 6. ArticleSerializer 클래스를 새로 정의해준 뒤 사용합니다.(더 아래에 정의 되기 때문에 새로 정의해주어야합니다.)
    class ArticleSerializer(serializers.ModelSerializer):

        class Meta:
            model = Article
            fields = '__all__'
    
    article = ArticleSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'content', 'created_at', 'updated_at', 'article')



class ArticleSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True, read_only=True)

    # Q 11. comment_count에 IntergerField로 comment_set을 count한 수를 불러옵니다.
    comment_count = serializers.IntegerField(
        source = 'comment_set.count',
        read_only=True
    )

    class Meta:
        model = Article
        fields = '__all__'
