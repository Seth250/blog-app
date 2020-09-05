from django.urls import path
from .views import UserProfileView, UserProfileEditView

app_name = 'userprofiles'

urlpatterns = [
	path('', UserProfileView.as_view(), name='profile'),
	path('edit/', UserProfileEditView.as_view(), name='profile_edit')
]