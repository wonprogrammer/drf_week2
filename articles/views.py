# render 또한 pure django 에서 사용하던 방식이므로 import하지 않는다.
# from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from articles.models import Article

# Create your views here.


# 기존의 pure django 에서 사용하던 templates를 사용하지 않고, rest_framework에서 api 브라우저에 직접 들어가서 조작 할 수 있게끔 만들어준다.
@api_view(['GET'])
def index(request):
    # pure django 에서 사용하던 방식
    # return HttpResponse('연결')
    
    articles = Article.objects.all()
    article = articles[0]
    
    # 이렇게 딕셔너리를 하나하나 만들어 주면 힘들기 떄문에 자동화해서 작성한다. (자동화 = 시리얼라이즈)
    article_date = {
        'title':article.title,
        'content':article.content,
        'create_at':article.create_at,
        'update_at':article.update_at,
    }
    
    # Response는 쿼리, 딕셔너리 등 json에서 다룰 수 있는 데이터만 받는다.
    return Response(article_date)