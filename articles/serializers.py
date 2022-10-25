# models에 정의된 objects들을 딕셔너리 형태 즉, JSON형태의 str으로 만들어 자동으로 response 할 수 있게 만들어 주는게 serializers
from dataclasses import field
from rest_framework import serializers
from articles.models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'