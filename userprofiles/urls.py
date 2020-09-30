from django.urls import path
from .views import (
	UserProfileView, 
	UserProfileEditView,
)

app_name = 'userprofiles'

urlpatterns = [
	path('edit-profile/', UserProfileEditView.as_view(), name='profile_edit'),
	path('<str:username>/', UserProfileView.as_view(), name='profile'),
]