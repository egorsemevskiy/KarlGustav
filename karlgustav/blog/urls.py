from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.blog_home, name="blog_home"),
    path('blog/article', views.article, name="article")
]