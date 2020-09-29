from django.urls import path
from .views import (
	PostListView,
	# UserPostListView,
	PostDetailView,
	PostCreateView,
	PostUpdateView,
	PostDeleteView,
	PostLikeToggleView,
	PostDislikeToggleView,
	CommentLikeToggleView,
	CommentDislikeToggleView,
	CategoryPostListView
)

app_name = 'blog'

urlpatterns = [
	path('', PostListView.as_view(), name='post_list'),
	path('create/', PostCreateView.as_view(), name='post_create'),
	# path('<str:user>/posts/', UserPostListView.as_view(), name='user_posts'),
	path('<str:slug>-<int:pk>/', PostDetailView.as_view(), name='post_detail'),
	path('<str:slug>-<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
	path('<str:slug>-<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
	path('<str:slug>-<int:pk>/like-toggle/', PostLikeToggleView.as_view(), name='post_like_toggle'),
	path('<str:slug>-<int:pk>/dislike-toggle/', PostDislikeToggleView.as_view(), name='post_dislike_toggle'),
	path('<str:slug>-<int:pk>/comments/<int:comment_pk>/like-toggle/', CommentLikeToggleView.as_view(), 
		name='comment_like_toggle'),
	path('<str:slug>-<int:pk>/comments/<int:comment_pk>/dislike-toggle/', CommentDislikeToggleView.as_view(), 
		name='comment_dislike_toggle'),
	path('<str:category>/', CategoryPostListView.as_view(), name='category_posts')
]
