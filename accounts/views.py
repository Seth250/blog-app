from django.shortcuts import render, redirect
from .forms import UserSignUpForm
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.views.generic import View, CreateView

# Create your views here.

# class UserRedirectView(View):

# 	def get(self, request, *args, **kwargs):
# 		if request.user.is_authenticated:
# 			return redirect('userprofiles:profile', user=request.user.profile.display_name)
# 		else:
# 			return redirect('accounts:login')


class UserCreateView(SuccessMessageMixin, CreateView):
	model = get_user_model()
	form_class = UserSignUpForm
	template_name = 'accounts/signup.html'
	success_message = 'Your Account has been succesfully Created, Login to Continue!'

	def get_success_url(self):
		return reverse("accounts:login")
