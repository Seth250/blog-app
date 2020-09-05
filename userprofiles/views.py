from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import UserUpdateForm, ProfileUpdateForm
from django.contrib import messages

# Create your views here.
class UserProfileView(View):

	def get(self, request, *args, **kwargs):
		user_form = UserUpdateForm(instance=request.user)
		profile_form = ProfileUpdateForm(instance=request.user.profile)
		context = {
			'user_form': user_form,
			'profile_form': profile_form
		}
		return render(request, 'userprofiles/profile.html', context)


class UserProfileEditView(View):
	def get(self, request, *args, **kwargs):
		user_form = UserUpdateForm(instance=request.user)
		profile_form = ProfileUpdateForm(instance=request.user.profile)
		context = {
			'user_form': user_form,
			'profile_form': profile_form
		}
		return render(request, 'userprofiles/profile_edit.html', context)

	def post(self, request, *args, **kwargs):
		user_form = UserUpdateForm(data=request.POST, instance=request.user)
		profile_form = ProfileUpdateForm(data=request.POST, files=request.FILES, instance=request.user.profile)
		if user_form.is_valid() and profile_form.is_valid():
			user_form.save()
			profile_form.save()
			messages.success(request, 'Your Profile has been Updated Successfully!')
			return redirect('userprofiles:profile')