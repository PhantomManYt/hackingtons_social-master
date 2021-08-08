from django.urls import path
from . import views
from .views import (
    PostListView,
    PostCreateView,
    PostDetailView,
    LikeView,
    DislikeView,
    PostDeleteView,
    PostUpdateView,
    UserPostListView,
    CommentCreateView,
    CommentDeleteView,
    AnnounceListView,
    AnnounceCreateView,
    UserListView,
)  

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),   
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('like/<int:pk>/', LikeView, name='like-post'),
    path('dislike/<int:pk>/', DislikeView, name='dislike-post'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/comment', CommentCreateView.as_view(), name='add-comment'),
    path('post/<int:pk>/comment/delete', CommentDeleteView.as_view(), name='delete-comment'),
    path('announcements/', AnnounceListView.as_view(), name="announcements"),
    path('announce/', AnnounceCreateView.as_view(), name='announce'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('error/', views.error, name="error"),
]
