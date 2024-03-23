from django.urls import path
from . import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('posts/', views.all_posts),
    path('funny/', views.all_funny),
    path('professional/', views.all_professional),
    path('posts/<int:id>/', views.all_posts),
    path('users/', views.all_users),
    path('users/<int:id>/', views.all_users),
    path('likes/', views.all_likes),
    path('likes/<int:id>/', views.all_likes),
    path('comments/', views.all_comments),
    path('comments/<int:id>/', views.all_comments),
    path('trackers/', views.all_trackers),
    path('trackers/<int:id>/', views.all_trackers),
    path('posts/savefile', views.saveFile),
    path('docs/', views.all_docs),
    path('forgot-password/', views.forgotPassword),
    path('docs/<int:id>/', views.all_docs),
    path('auth/', views.login),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)