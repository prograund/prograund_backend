from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.all_posts),
    path('posts/<int:id>/', views.all_posts),
    path('users/', views.all_users),
    path('users/<int:id>/', views.all_users),
    path('likes/', views.all_likes),
    path('likes/<int:id>/', views.all_likes),
    path('comments/', views.all_comments),
    path('comments/<int:id>/', views.all_comments),
    path('follows/', views.all_follows),
    path('follows/<int:id>/', views.all_follows),
]