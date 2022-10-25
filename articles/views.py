# render 또한 pure django 에서 사용하던 방식이므로 import하지 않는다.
# from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from articles.models import Article
from articles.serializers import ArticleSerializer
from drf_yasg.utils import swagger_auto_schema


# Create your views here.

''' 아래 def articleAPI(request) 함수 코드를 class ArticleList(APIView) 안에 넣으므로써 더욱 유용하게 사용할 수 있다.

# 기존의 pure django 에서 사용하던 templates를 사용하지 않고, rest_framework에서 api 브라우저에 직접 들어가서 조작 할 수 있게끔 만들어준다.
@api_view(['GET', 'POST'])
def articleAPI(request):
    if request.method == 'GET':
    # pure django 에서 사용하던 방식
    # return HttpResponse('연결')
    
        articles = Article.objects.all()
        
        
        # 아래와 같이 딕셔너리를 하나하나 만들어 주면 힘들기 떄문에 자동화해서 작성한다. (자동화 = 시리얼라이즈)
        article_date = {
            'title':article.title,
            'content':article.content,
            'create_at':article.create_at,
            'update_at':article.update_at,
        }
        

        # serializers 선언 방법 / many=True는 article 하나가 아닌 여러개인 list 형태로 가져온다.
        serializer = ArticleSerializer(articles, many=True)
        
        # Response는 쿼리, 딕셔너리 등 json에서 다룰 수 있는 데이터만 받는다. + serializers에 들어있는 데이터를 가져오기 위해선 '.data'를 붙여줘야 한다.
        return Response(serializer.data)

    elif request.method == 'POST':
        # POST된 데이터를 어떻게 모델에서 정의된 articles형태로 바꿔줄 것인가? 디시리얼라이징
        serializer = ArticleSerializer(data = request.data)

        # 유효성 검사
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            # 백엔드 사용자가 볼 수 있는 error 메세지
            print(serializer.errors)
            # 본래 프론트에 어떠한 부분 때문에 에러가 났는지 보여주는것은 좋지않다. just 404error 메세지를 보여 줄 수 있다(주면 좋다).
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
'''


# class 장점 : 상속이 가능하다.
class ArticleList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        if request.method == 'GET':
            articles = Article.objects.all()
            serializer = ArticleSerializer(articles, many=True)
            return Response(serializer.data)

    @swagger_auto_schema(request_body=ArticleSerializer)
    def post(self, request, format=None):
        serializer = ArticleSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




''' 마찬가지로 각각의 method를 정의해놓은 def articleDetailAPI를 class ArticleDetail(APIView)로 정의
@api_view(['GET', 'PUT', 'DELETE'])
def articleDetailAPI(request, article_id):
    if request.method == 'GET':
        # article = Article.objects.get(id=article_id)
        article = get_object_or_404(Article, id=article_id)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    elif request.method == 'PUT':
        article = get_object_or_404(Article, id=article_id)
        serializer = ArticleSerializer(article, data = request.data)    # 데이터를 수정한 데이터로 다시 받아와

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    elif request.method == 'DELETE':
        article = get_object_or_404(Article, id=article_id)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
'''


class ArticleDetail(APIView):

    def get(self, request, article_id, format=None):
        article = get_object_or_404(Article, id=article_id)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    def put(self, request, article_id, format=None):
        article = get_object_or_404(Article, id=article_id)
        serializer = ArticleSerializer(article, data = request.data)    # 데이터를 수정한 데이터로 다시 받아와

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, article_id, format=None):
        article = get_object_or_404(Article, id=article_id)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
