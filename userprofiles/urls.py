from django.urls import path
from . import views


app_name = 'userprofiles'

urlpatterns = [
	path('edit-profile/', views.UserProfileEditView.as_view(), name='profile_edit'),
	path('<str:username>/', views.UserProfileView.as_view(), name='profile'),
	path('posts/liked/', views.UserLikedPostsView.as_view(), name='liked_posts'),
	path('posts/disliked/', views.UserDislikedPostsView.as_view(), name='disliked_posts'),
	path('drafts/', views.UserDraftedPostsView.as_view(), name='drafted_posts'),
	path('drafts/<str:slug>-<int:pk>/', views.UserDraftPreviewView.as_view(), name='draft_preview'),
	path('drafts/<str:slug>-<int:pk>/publish/', views.UserDraftPublishView.as_view(), name='draft_publish'),
	path('drafts/<str:slug>-<int:pk>/update/', views.UserDraftUpdateView.as_view(), name='draft_update'),
	path('drafts/<str:slug>-<int:pk>/delete/', views.UserDraftDeleteView.as_view(), name='draft_delete'),
	path('<str:username>/posts/', views.UserPublishedPostsView.as_view(), name='user_published_posts'),
	path('<str:username>/comments/', views.UserCommentListView.as_view(), name='user_comments')
]