from django.urls import path
from . import views


app_name = 'userprofiles'

urlpatterns = [
	path('edit-profile/', views.UserProfileEditView.as_view(), name='profile_edit'),
	path('liked/posts/', views.UserLikedPostsView.as_view(), name='user_liked_posts'),
	path('disliked/posts/', views.UserDislikedPostsView.as_view(), name='user_disliked_posts'),
	path('drafts/', views.UserDraftedPostsView.as_view(), name='user_drafted_posts'),
	path('drafts/<str:slug>-<int:pk>/', views.UserDraftPreviewView.as_view(), name='user_draft_preview'),
	path('drafts/<str:slug>-<int:pk>/publish/', views.UserDraftPublishView.as_view(), name='user_draft_publish'),
	path('drafts/<str:slug>-<int:pk>/update/', views.UserDraftUpdateView.as_view(), name='user_draft_update'),
	path('drafts/<str:slug>-<int:pk>/delete/', views.UserDraftDeleteView.as_view(), name='user_draft_delete'),
	path('drafts/<str:category>/', views.CategoryUserDraftedPosts.as_view(), name='category_user_drafts'),
	path('<str:username>/', views.UserProfileView.as_view(), name='profile'),
	path('<str:username>/posts/', views.UserPublishedPostsView.as_view(), name='user_published_posts'),
	path('<str:username>/comments/', views.UserCommentListView.as_view(), name='user_comments'),
]