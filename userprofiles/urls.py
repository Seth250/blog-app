from django.urls import path
from .views import (
	UserProfileView, 
	UserProfileEditView,
	UserDraftedPostsView,
	UserLikedPostsView,
	UserDislikedPostsView
)

app_name = 'userprofiles'

urlpatterns = [
	path('', UserProfileView.as_view(), name='profile'),
	path('edit/', UserProfileEditView.as_view(), name='profile_edit'),
	path('activity/drafts/', UserDraftedPostsView.as_view(), name='drafted_posts'),
	path('activity/liked-posts/', UserLikedPostsView.as_view(), name='liked_posts'),
	path('activity/disliked-posts/', UserDislikedPostsView.as_view(), name='disliked_posts')
]