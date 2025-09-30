from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, CommentUpdateView, CommentDeleteView

urlpatterns = [
    # path('', views.home, name="blog-home"),
    path('about/', views.about, name="blog-about"),

    path('', PostListView.as_view(), name="blog-home"),
    path('post-new/', PostCreateView.as_view(), name="blog-new"),
    path('post/<int:pk>/', PostDetailView.as_view(), name="blog-detail"),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name="blog-update"),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name="blog-delete"),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
    path('like/<int:pk>/', views.like_post, name='like-post'),
    path('dislike/<int:pk>/', views.dislike_post, name='dislike-post'),
    path('', views.home, name='blog-home'),
    path('comment/<int:pk>/', views.add_comment, name='add-comment'),


]