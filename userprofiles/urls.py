from django.urls import path
from .views import (
	UserProfileView, 
	UserProfileEditView,
	UserDraftedPostsView,
	UserDraftPreviewView,
	UserDraftPublishView,
	UserLikedPostsView,
	UserDislikedPostsView
)

app_name = 'userprofiles'

urlpatterns = [
	path('', UserProfileView.as_view(), name='profile'),
	path('edit/', UserProfileEditView.as_view(), name='profile_edit'),
	path('activity/drafts/', UserDraftedPostsView.as_view(), name='drafted_posts'),
	path('activity/drafts/<str:slug>-<int:pk>/', UserDraftPreviewView.as_view(), name='draft_preview'),
	path('activity/drafts/<str:slug>-<int:pk>/publish/', UserDraftPublishView.as_view(), name='draft_publish'),
	path('activity/liked-posts/', UserLikedPostsView.as_view(), name='liked_posts'),
	path('activity/disliked-posts/', UserDislikedPostsView.as_view(), name='disliked_posts')
]