from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import UserUpdateForm
from django.contrib import messages

# Create your views here.
class UserProfileView(View):

	def get(self, request, *args, **kwargs):
		form = UserUpdateForm(instance=request.user)
		return render(request, 'userprofiles/profile.html', {'form': form})

	def post(self, request, *args, **kwargs):
		form = UserUpdateForm(data=request.POST, files=request.FILES, instance=request.user)
		if form.is_valid():
			form.save()
			messages.success(request, 'Your Profile has been Updated Successfully!')
			return redirect('userprofiles:profile')
