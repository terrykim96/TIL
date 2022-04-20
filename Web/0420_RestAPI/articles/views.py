from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse

from .models import Article
from .serializers import (
    ArticleListSerializer,
    ArticleSerializer
)


# Create your views here.
@api_view(['GET', 'POST'])
def article_list(request):

    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArticleListSerializer(data=request.data)    # 사용자 요청 데이터 바인딩
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)        # 생성된 데이터 응답


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)

    serializer = ArticleSerializer(article)

    return Response(serializer.data)