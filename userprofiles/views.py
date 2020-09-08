from django.shortcuts import render, redirect
from django.views.generic import (
	View,
	DetailView,
	UpdateView,
	DeleteView
)
from .forms import UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from blog.forms import PostForm
from blog.views import CustomListView
from django.views.generic.detail import SingleObjectMixin
from django.urls import reverse

# Create your views here.
class UserProfileView(View):

	def get(self, request, *args, **kwargs):
		context = {
			'num_drafted': request.user.posts.drafted().count(),
			'num_published': request.user.posts.published().count(),
			'num_liked': request.user.post_likes.count(),
			'num_disliked': request.user.post_dislikes.count()
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


class UserDraftedPostsView(CustomListView):
	template_name = 'userprofiles/draft_list.html'

	def get_queryset(self):
		return self.request.user.posts.drafted()


class UserDraftPreviewView(DetailView):
	template_name = 'userprofiles/draft_preview.html'

	def get_queryset(self):
		return self.request.user.posts.drafted()


class UserDraftUpdateView(UpdateView):
	form_class = PostForm
	query_pk_and_slug = True
	# template_name = 'userprofiles/draft_update.html'

	def get_queryset(self):
		return self.request.user.posts.drafted()

	def get_success_url(self):
		return reverse('userprofiles:draft_preview', kwargs={'slug': self.object.slug, 'pk': self.object.pk})


class UserDraftDeleteView(DeleteView):
	query_pk_and_slug = True
	# template_name = 'userprofiles/draft_update.html'

	def get_queryset(self):
		return self.request.user.posts.drafted()

	def get_success_url(self):
		return reverse('userprofiles:drafted_posts')


class UserDraftPublishView(SingleObjectMixin, View):
	query_pk_and_slug = True

	def get_queryset(self):
		return self.request.user.posts.drafted()

	def post(self, request, *args, **kwargs):
		obj = self.get_object()
		obj.publish()
		return redirect(obj.get_absolute_url())


class UserLikedPostsView(CustomListView):

	def get_queryset(self):
		return self.request.user.post_likes.all()


class UserDislikedPostsView(CustomListView):

	def get_queryset(self):
		return self.request.user.post_dislikes.all()

