from django.urls import path
from . import views


app_name = 'blog'

urlpatterns = [
	path('posts/', views.PostListView.as_view(), name='post_list'),
	path('posts/create/', views.PostCreateView.as_view(), name='post_create'),
	path('posts/<str:slug>-<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
	path('posts/<str:slug>-<int:pk>/update/', views.PostUpdateView.as_view(), name='post_update'),
	path('posts/<str:slug>-<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
	path('posts/<str:slug>-<int:pk>/like-toggle/', views.PostLikeToggleView.as_view(), name='post_like_toggle'),
	path('posts/<str:slug>-<int:pk>/dislike-toggle/', views.PostDislikeToggleView.as_view(), name='post_dislike_toggle'),
	path('posts/<str:slug>-<int:pk>/comments/<int:comment_pk>/like-toggle/', views.CommentLikeToggleView.as_view(), 
		name='comment_like_toggle'),
	path('posts/<str:slug>-<int:pk>/comments/<int:comment_pk>/dislike-toggle/', views.CommentDislikeToggleView.as_view(), 
		name='comment_dislike_toggle'),
	path('posts/<str:category>/', views.CategoryPostListView.as_view(), name='category_posts')
]
