from django.urls import path
from . import views

app_name='core'

urlpatterns = [
    path('v1/', views.listAPI.as_views(), name='list'),
]
