from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.all_posts),
    path('posts/<int:id>/', views.all_posts),
]