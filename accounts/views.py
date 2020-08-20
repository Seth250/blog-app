from django.shortcuts import render, redirect
from .forms import UserSignUpForm, UserUpdateForm
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.views.generic import (
	View,
	CreateView,
	UpdateView,
)


# Create your views here.

class RedirectView(View):

	def get(self, request, *args, **kwargs):
		if request.user.is_authenticated:
			return redirect('accounts:profile')
		else:
			return redirect('accounts:login')


class UserCreateView(SuccessMessageMixin, CreateView):
	model = get_user_model()
	form_class = UserSignUpForm
	template_name = 'accounts/signup.html'
	success_message = 'Your Account has been succesfully Created, Login to Continue!'

	def get_success_url(self):
		return reverse("accounts:login")


# def profile(request):
# 	if request.method == 'POST':
# 		form = UserUpdateForm(data=request.POST, files=request.FILES, instance=request.user)
# 		if form.is_valid():
# 			form.save()
# 			return redirect('accounts:profile')

# 	else:
# 		form = UserUpdateForm(instance=request.user)

# 	context = {
# 		'form': form,
# 	}

# 	return render(request, 'accounts/profile.html', context)


class UserUpdateView(View):
	form_class = UserUpdateForm
	template_name = 'accounts/profile.html'
	success_message = 'Your Profile has been Updated Successfully!'

	def get(self, request, *args, **kwargs):
		form = self.form_class(instance=request.user)
		return render(request, self.template_name, {'form': form})

	def post(self, request, *args, **kwargs):
		form = self.form_class(data=request.POST, files=request.FILES, instance=request.user)
		if form.is_valid():
			form.save()
			messages.success(request, self.success_message)
			return redirect('accounts:profile')
