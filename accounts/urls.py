from django.urls import path
from django.contrib.auth import views as auth_views
from .views import UserCreateView, UserUpdateView #profile
from .forms import CustomAuthenticationForm

app_name = 'accounts'

urlpatterns = [
	path('signup/', UserCreateView.as_view(), name='signup'),
	path('login/', auth_views.LoginView.as_view(
			template_name='accounts/login.html',
			redirect_authenticated_user=True, 
			authentication_form=CustomAuthenticationForm), name='login'),
	path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
	# path('profile/', profile, name='profile'),
	path('profile/', UserUpdateView.as_view(), name='profile'),
]