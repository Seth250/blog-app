from django.shortcuts import render
from .forms import UserSignUpForm
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.views.generic import (
	CreateView)


# Create your views here.

class UserCreateView(CreateView):
	model = get_user_model()
	template_name = 'accounts/signup.html'
	form_class = UserSignUpForm

	def get_success_url(self):
		return reverse("accounts:login")

	def form_valid(self, form):
		return super().form_valid(form)