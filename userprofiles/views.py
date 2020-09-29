from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (
	View,
	DetailView,
	UpdateView,
	DeleteView
)
from .forms import UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from .models import Profile
from blog.forms import PostForm
from blog.views import CustomListView, PostListView
from django.contrib.auth import get_user_model
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.detail import SingleObjectMixin
from django.urls import reverse
from django.core.exceptions import PermissionDenied

# Create your views here.
class OwnerRequiredMixin(SingleObjectMixin):

	def dispatch(self, request, *args, **kwargs):
		if self.get_object().author != request.user:
			raise PermissionDenied

		return super(OwnerRequiredMixin, self).dispatch(request, *args, **kwargs)


class UserProfileView(View):

	def get(self, request, *args, **kwargs):
		user_obj = get_object_or_404(
			get_user_model().objects.select_related('profile'), 
			username__iexact=kwargs['username']
		)
		context = {
			'user_obj': user_obj,
			'num_drafted': user_obj.posts.drafted().count(),
			'num_published': user_obj.posts.published().count(),
			'num_liked': user_obj.post_likes.count(),
			'num_disliked': user_obj.post_dislikes.count()
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
			return redirect('userprofiles:profile', username=request.user.username)

		return render(request, 'userprofiles/profile_edit.html', {'user_form': user_form, 'profile_form': profile_form})


class UserPublishedPostsView(PostListView):

	def get_queryset(self):
		user = get_object_or_404(get_user_model(), username__iexact=self.kwargs['username'])
		return super(UserPublishedPostsView, self).get_queryset().filter(author=user)


class UserDraftedPostsView(CustomListView):
	template_name = 'userprofiles/draft_list.html'

	def get_queryset(self):
		return self.request.user.posts.select_related('category').drafted()


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
		messages.info(self.request, 'Draft has been Updated!')
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
		messages.success(request, 'Post has been Published Successfully!')
		return redirect(obj.get_absolute_url())


class UserLikedPostsView(CustomListView):

	def get_queryset(self):
		return self.request.user.post_likes.all()


class UserDislikedPostsView(CustomListView):

	def get_queryset(self):
		return self.request.user.post_dislikes.all()

