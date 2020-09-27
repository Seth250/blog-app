from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.views.generic.detail import SingleObjectMixin
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.db import transaction
from django.urls import reverse
from django.views.generic import (
	View,
	ListView,
	DetailView,
	CreateView,
	UpdateView,
	DeleteView,
)

# Create your views here.

#consider checking multipleobjectmixin application in crozoff
class CustomListView(ListView):
	paginate_by = 2


class PostListView(CustomListView):

	def get_queryset(self):
		return Post.objects.select_related('author__profile', 'category').published()


# change url name to something else (I dont know what you should change it to)
# class UserPostListView(CustomListView):

	# def get_queryset(self):
	# 	return Post.objects.published().filter(author__url_name=self.kwargs.get('user'))


class PostDetailView(SingleObjectMixin, View):
	query_pk_and_slug = True

	def get_queryset(self):
		return Post.objects.published()

	def get(self, request, *args, **kwargs):
		obj = self.get_object()
		form = CommentForm()
		context = {
			'object': obj,
			'comment_form': form
		}
		return render(request, 'blog/post_detail.html', context)

	def post(self, request, *args, **kwargs):
		form = CommentForm(data=request.POST)
		if form.is_valid():
			with transaction.atomic():
				obj = self.get_object()
				instance = form.save(commit=False)
				instance.post = obj
				instance.author = request.user
				instance.save()

		# return redirect('blog:post_detail', pk=obj.pk, slug=obj.slug)
		return redirect(obj.get_absolute_url())


class PostCreateView(CreateView):
	model = Post
	form_class = PostForm

	def get_context_data(self, **kwargs):
		kwargs['action'] = 'create'
		return super(PostCreateView, self).get_context_data(**kwargs)

	def get_success_url(self):
		return reverse('userprofiles:draft_preview', kwargs={'slug': self.object.slug, 'pk': self.object.pk})

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)


class PostUpdateView(UpdateView):
	# model = Post
	query_pk_and_slug = True
	form_class = PostForm

	def get_queryset(self):
		return self.request.user.posts.published()

	def get_context_data(self, **kwargs):
		kwargs['action'] = 'update'
		return super(PostUpdateView, self).get_context_data(**kwargs)

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)


class PostDeleteView(DeleteView):
	query_pk_and_slug = True

	def get_queryset(self):
		return self.request.user.posts.published()

	def get_success_url(self):
		return reverse('blog:post_list')


class ActionManagerMixin(SingleObjectMixin):

	def get_object_action_managers(self):
		obj = self.get_object()
		return [obj.likes, obj.dislikes] if self.action == 'like_toggle' else [obj.dislikes, obj.likes]


class ObjectActionToggleView(ActionManagerMixin, View):

	# def get(self, request, *args, **kwargs):
	# 	main_obj_manager, opp_obj_manager = self.get_object_action_managers()

	# 	if request.user in main_obj_manager.all():
	# 		main_obj_manager.remove(request.user)

	# 	elif request.user in opp_obj_manager.all():
	# 		opp_obj_manager.remove(request.user)
	# 		main_obj_manager.add(request.user)

	# 	else:
	# 		main_obj_manager.add(request.user)

	# 	return redirect('blog:post_detail', pk=self.kwargs['pk'], slug=self.kwargs['slug'])

	def post(self, request, *args, **kwargs):
		main_obj_manager, opp_obj_manager = self.get_object_action_managers()

		if request.user in main_obj_manager.all():
			main_obj_manager.remove(request.user)

		elif request.user in opp_obj_manager.all():
			opp_obj_manager.remove(request.user)
			main_obj_manager.add(request.user)

		else:
			main_obj_manager.add(request.user)

		return JsonResponse({'status': 'ok'}, status=200)


class UserPostLikeToggleView(ObjectActionToggleView):
	# model = Post
	query_pk_and_slug = True
	action = 'like_toggle'

	def get_queryset(self):
		return Post.objects.published()


class UserPostDislikeToggleView(ObjectActionToggleView):
	# model = Post
	query_pk_and_slug = True
	action = 'dislike_toggle'

	def get_queryset(self):
		return Post.objects.published()


class UserCommentLikeToggleView(ObjectActionToggleView):
	model = Comment
	pk_url_kwarg = 'comment_pk'
	action = 'like_toggle'


class UserCommentDislikeToggleView(ObjectActionToggleView):
	model = Comment
	pk_url_kwarg = 'comment_pk'
	action = 'dislike_toggle'
