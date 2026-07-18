from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.landing, name='landing'),
    path('article/<int:pk>/', views.article_detail, name='article_detail'),
    path('post/new/', views.create_article, name='create_article'),
]
