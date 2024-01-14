from django.shortcuts import render
from .models import Article
from rest_framework import mixins, generics, permissions
from .serialzers import ArticleSerializer

# Create your views here.
class listAPI(generics.ListAPIView):
    serializer_class = ArticleSerializer
    permissions_classes = [permissions.AllowAny]
    queryset = Article.objects.all()
