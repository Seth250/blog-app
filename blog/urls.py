from django.urls import path
from .views import (
	PostListView,
	PostDetailView,
	PostCreateView,
	PostUpdateView,
)

app_name = 'blog'

urlpatterns = [
	path('', PostListView.as_view(), name='post_list'),
	path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
	path('create/', PostCreateView.as_view(), name='post_create'),
	path('<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
]