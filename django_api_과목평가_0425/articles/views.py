from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django.shortcuts import get_object_or_404

from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer
from .models import Article, Comment

@api_view(['GET', 'POST'])
def article_list(request):
    # Q 1. request.method가 'GET'일 경우, Article 모델의 모든 게시글 정보를 불러옵니다.
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)
    
    # Q 2. request.method가 'POST'일 경우, 사용자가 요청한 데이터를 바인딩하여 보여주고, 입력한 결과가 올바른 형식이라면 DB에 저장합니다.
    elif request.method == 'POST':
        serializer = ArticleListSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)     # 사용자가 입력한 pk에 맞는 게시글 정보를 불러옵니다. 없다면 404 오류를 불러옵니다.

    # Q 3. request.method가 'GET'일 경우, 그 게시글의 정보를 반환합니다.
    if request.method == 'GET':
        serializer = ArticleSerializer(article)

        return Response(serializer.data)

    # Q 4. request.method가 'DELETE'일 경우, 게시글을 DB에서 지우고 key가 'delete', value가 artist_pk인 json 데이터를 반환합니다.
    if request.method == 'DELETE':
        article.delete()
        data = {
            'delete': f'{article_pk}'
        }

        return Response(data)

    # Q 5. request.method가 'PUT'일 경우, 게시글 수정을 해줍니다. instance로 초기 값을 현재 값으로 설정해줍니다.
    if request.method == 'PUT':
        serializer = ArticleSerializer(data=request.data, instance=article)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)



@api_view(['GET'])
def comment_list(request):
    # Q 7.  Comment 클래스의 모든 댓글 정보를 받아온 후 반환합니다.
    comments = Comment.objects.all()
    serializer = CommentSerializer(comments, many=True)
    
    return Response(serializer.data)

@api_view(['POST'])
def comment_create(request, article_pk):
    # Q 8. Comment가 유효하면 article에 댓글을 저장합니다.
    article = get_object_or_404(Article, pk=article_pk)
    serializer = CommentSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'DELETE'])
def comment_detail(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk) # 사용자가 입력한 pk에 맞는 댓글 정보를 불러옵니다. 없다면 404 오류를 불러옵니다.

    # Q 9. request.method가 'GET'일 경우, 선택한 댓글의 정보를 반환합니다.
    if request.method == 'GET':
        serializer = CommentSerializer(comment)

        return Response(serializer.data)

    # Q 10. request.method가 'DELETE'일 경우, 댓글을 DB에서 지우고 key가 'delete', value가 comment_pk인 json 데이터를 반환합니다.
    elif request.method == 'DELETE':
        comment.delete()
        data = {
            'delete': f'{comment_pk}'
        }

        return Response(data)
