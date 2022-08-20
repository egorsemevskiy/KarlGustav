from django.urls import path
from . import views

urlpatterns = [
    path('login/' , views.loging_page, name="login_page" ),
    path('logout/' , views.logoutUser, name="logout-user" ),
    path('register/' , views.registerUser , name="register_page" ),

    path('blog/', views.blog_home, name="blog_home"),
    path('blog/<int:pk>/', views.article, name="article"),

    path('blog/create-article/', views.createArticle, name='create-article'),
    path('blog/update-article/<int:pk>', views.updateArticle, name='update-article'),
    path('blog/delete-article/<int:pk>', views.deleteArticle, name='delete-article'),
]