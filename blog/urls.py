from django.urls import path
from .views import (
	PostListView,
	PostDetailView,
	PostCreateView,
	PostUpdateView,
	PostDeleteView,
	PostLikeToggleView,
	PostDislikeToggleView,
	CommentLikeToggleView,
	CommentDislikeToggleView,
	CategoryPostListView,
	UserPublishedPostsView,
	DraftedPostsView,
	DraftPreviewView,
	DraftUpdateView,
	DraftDeleteView,
	DraftPublishView,
	LikedPostsView,
	DislikedPostsView,
	UserCommentListView
)

app_name = 'blog'

urlpatterns = [
	path('posts/', PostListView.as_view(), name='post_list'),
	path('posts/create/', PostCreateView.as_view(), name='post_create'),
	path('posts/<str:slug>-<int:pk>/', PostDetailView.as_view(), name='post_detail'),
	path('posts/<str:slug>-<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
	path('posts/<str:slug>-<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
	path('posts/<str:slug>-<int:pk>/like-toggle/', PostLikeToggleView.as_view(), name='post_like_toggle'),
	path('posts/<str:slug>-<int:pk>/dislike-toggle/', PostDislikeToggleView.as_view(), name='post_dislike_toggle'),
	path('posts/<str:slug>-<int:pk>/comments/<int:comment_pk>/like-toggle/', CommentLikeToggleView.as_view(), 
		name='comment_like_toggle'),
	path('posts/<str:slug>-<int:pk>/comments/<int:comment_pk>/dislike-toggle/', CommentDislikeToggleView.as_view(), 
		name='comment_dislike_toggle'),
	path('posts/liked/', LikedPostsView.as_view(), name='liked_posts'),
	path('posts/disliked/', DislikedPostsView.as_view(), name='disliked_posts'),
	path('posts/<str:category>/', CategoryPostListView.as_view(), name='category_posts'),
	path('drafts/', DraftedPostsView.as_view(), name='drafted_posts'),
	path('drafts/<str:slug>-<int:pk>/', DraftPreviewView.as_view(), name='draft_preview'),
	path('drafts/<str:slug>-<int:pk>/publish/', DraftPublishView.as_view(), name='draft_publish'),
	path('drafts/<str:slug>-<int:pk>/update/', DraftUpdateView.as_view(), name='draft_update'),
	path('drafts/<str:slug>-<int:pk>/delete/', DraftDeleteView.as_view(), name='draft_delete'),
	path('<str:username>/posts/', UserPublishedPostsView.as_view(), name='user_published_posts'),
	path('<str:username>/comments/', UserCommentListView.as_view(), name='user_comments')
]
