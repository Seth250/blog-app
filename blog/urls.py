from django.urls import path
from .views import (
	PostListView,
	UserPostListView,
	PostDetailView,
	PostCreateView,
	PostUpdateView,
	UserPostLikeToggleView,
	UserPostDislikeToggleView,
	UserCommentLikeToggleView,
	UserCommentDislikeToggleView
)

app_name = 'blog'

urlpatterns = [
	path('', PostListView.as_view(), name='post_list'),
	path('<str:username>/posts/', UserPostListView.as_view(), name='user_posts'),
	path('<str:slug>-<int:pk>/', PostDetailView.as_view(), name='post_detail'),
	path('create/', PostCreateView.as_view(), name='post_create'),
	path('<str:slug>-<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
	path('<str:slug>-<int:pk>/like-toggle/', UserPostLikeToggleView.as_view(), name='post_like_toggle'),
	path('<str:slug>-<int:pk>/dislike-toggle/', UserPostDislikeToggleView.as_view(), name='post_dislike_toggle'),
	path('<str:slug>-<int:pk>/comments/<int:comment_pk>/like-toggle/', UserCommentLikeToggleView.as_view(), 
		name='comment_like_toggle'),
	path('<str:slug>-<int:pk>/comments/<int:comment_pk>/dislike-toggle/', UserCommentDislikeToggleView.as_view(), 
		name='comment_dislike_toggle')
]