from django.urls import path
from .views import (
	UserProfileView, 
	UserProfileEditView,
	UserPublishedPostsView,
	UserDraftedPostsView,
	UserDraftPreviewView,
	UserDraftUpdateView,
	UserDraftDeleteView,
	UserDraftPublishView,
	UserLikedPostsView,
	UserDislikedPostsView
)

app_name = 'userprofiles'

urlpatterns = [
	path('edit-profile/', UserProfileEditView.as_view(), name='profile_edit'),
	path('drafts/', UserDraftedPostsView.as_view(), name='drafted_posts'),
	path('drafts/<str:slug>-<int:pk>/', UserDraftPreviewView.as_view(), name='draft_preview'),
	path('drafts/<str:slug>-<int:pk>/publish/', UserDraftPublishView.as_view(), name='draft_publish'),
	path('drafts/<str:slug>-<int:pk>/update/', UserDraftUpdateView.as_view(), name='draft_update'),
	path('drafts/<str:slug>-<int:pk>/delete/', UserDraftDeleteView.as_view(), name='draft_delete'),
	path('liked-posts/', UserLikedPostsView.as_view(), name='liked_posts'),
	path('disliked-posts/', UserDislikedPostsView.as_view(), name='disliked_posts'),
	path('<str:username>/', UserProfileView.as_view(), name='profile'),
	path('<str:username>/posts/', UserPublishedPostsView.as_view(), name='published_posts')
]