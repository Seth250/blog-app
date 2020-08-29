from django.urls import path
from .views import (
	PostListView,
	UserPostListView,
	PostDetailView,
	PostCreateView,
	PostUpdateView,
	UserPostLikeToggleView,
	UserPostDislikeToggleView
)

app_name = 'blog'

urlpatterns = [
	path('', PostListView.as_view(), name='post_list'),
	path('<str:username>/posts/', UserPostListView.as_view(), name='user_posts'),
	path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
	path('create/', PostCreateView.as_view(), name='post_create'),
	path('<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
	path('<int:pk>/like-toggle/', UserPostLikeToggleView.as_view(), name='post_like_toggle'),
	path('<int:pk>/dislike-toggle/', UserPostDislikeToggleView.as_view(), name='post_dislike_toggle')
]