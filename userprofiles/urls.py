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
	path('<str:user>/', UserProfileView.as_view(), name='profile'),
	path('<str:user>/edit-profile/', UserProfileEditView.as_view(), name='profile_edit'),
	path('<str:user>/posts/')
	path('<str:user>/drafts/', UserDraftedPostsView.as_view(), name='drafted_posts'),
	path('<str:user>/drafts/<str:slug>-<int:pk>/', UserDraftPreviewView.as_view(), name='draft_preview'),
	path('<str:user>/drafts/<str:slug>-<int:pk>/publish/', UserDraftPublishView.as_view(), name='draft_publish'),
	path('<str:user>/drafts/<str:slug>-<int:pk>/update/', UserDraftUpdateView.as_view(), name='draft_update'),
	path('<str:user>/drafts/<str:slug>-<int:pk>/delete/', UserDraftDeleteView.as_view(), name='draft_delete'),
	path('<str:user>/liked-posts/', UserLikedPostsView.as_view(), name='liked_posts'),
	path('<str:user>/disliked-posts/', UserDislikedPostsView.as_view(), name='disliked_posts')
]