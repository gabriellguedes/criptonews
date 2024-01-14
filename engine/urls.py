from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from rest_framework import routers
from engine.core import viewsets

route = routers.DefaultRouter()
route.register(r'api', viewsets.ArticleViewSet, basename="Articles")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls)),
]
