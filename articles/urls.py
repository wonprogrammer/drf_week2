from django.urls import path, include
from articles import views

urlpatterns = [
    # class 로 view에서 선언시 "views.class이름.as_view()" 형식으로 써줘야 함
    path('', views.ArticleList.as_view(), name='index'),
    path('<int:article_id>/', views.ArticleDetail.as_view(), name='article_view'),
]