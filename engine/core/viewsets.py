from rest_framework import viewsets
from . import serializers
from . import models

class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ArticleSerializer
    queryset = models.Article.objects.all()
