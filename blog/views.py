from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Count
from .models import Post, Comment, Category
from .forms import PostForm, CommentForm
from django.conf import settings
from django.views.generic.detail import SingleObjectMixin
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.http import JsonResponse
from django.db import transaction
from django.urls import reverse
from django.db.models import Prefetch
from urllib import parse
from django.views.generic import (
	View,
	ListView,
	DetailView,
	CreateView,
	UpdateView,
	DeleteView,
)

# Create your views here.


class CustomListView(ListView):
	paginate_by = 4


class PostListView(CustomListView):

	def get_queryset(self):
		return Post.objects.select_related('author__profile', 'category').published()


class PostDetailView(SingleObjectMixin, View):
	query_pk_and_slug = True

	def get_queryset(self):
		comments = Prefetch(
			'comments', 
			queryset=Comment.objects.select_related('author').prefetch_related('likes', 'dislikes')
		)
		return Post.objects.select_related('author__profile', 'category').prefetch_related(
			comments, 'likes', 'dislikes'
		).published()

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

		return redirect(obj.get_absolute_url())


class PostCreateView(CreateView):
	model = Post
	form_class = PostForm

	def get_context_data(self, **kwargs):
		kwargs['action'] = 'create'
		return super(PostCreateView, self).get_context_data(**kwargs)

	def get_success_url(self):
		return reverse('userprofiles:user_draft_preview', kwargs={'slug': self.object.slug, 'pk': self.object.pk})

	def form_valid(self, form):
		form.instance.author = self.request.user
		messages.info(self.request, 'Draft has been Created!')
		return super().form_valid(form)


class PostUpdateView(UpdateView):
	query_pk_and_slug = True
	form_class = PostForm

	def get_queryset(self):
		return self.request.user.posts.published()

	def get_context_data(self, **kwargs):
		kwargs['action'] = 'update'
		return super(PostUpdateView, self).get_context_data(**kwargs)

	def form_valid(self, form):
		# form.instance.author = self.request.user
		messages.success(self.request, 'Your Post has been Successfully Updated!')
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

	def post(self, request, *args, **kwargs):
		if not request.user.is_authenticated:
			# the reason we're using request.Meta... and not request.path or request.get_full_path() to get the
			# next url (the url the user should be redirected to after logging in i.e the page they were on before 
			# they were asked to login) is because it returns the url for like/dislike toggle and GET requests 
			# are not allowed on that url (only ajax POST is allowed), thereby resulting in a 405 error.
			# so yeah, we'll like to avoid that 
			redirect_to = parse.urlparse(request.META['HTTP_REFERER']).path
			response = {'redirect_url': f"{reverse(settings.LOGIN_URL)}?next={redirect_to}"}
			return JsonResponse(response, status=401)

		if request.is_ajax():
			main_obj_manager, opp_obj_manager = self.get_object_action_managers()

			if request.user in main_obj_manager.all():
				main_obj_manager.remove(request.user)

			elif request.user in opp_obj_manager.all():
				opp_obj_manager.remove(request.user)
				main_obj_manager.add(request.user)

			else:
				main_obj_manager.add(request.user)

			response = {
				'main_elem_count': main_obj_manager.count(),
				'opp_elem_count': opp_obj_manager.count()
			}

			return JsonResponse(response, status=200)


class PostLikeToggleView(ObjectActionToggleView):
	# model = Post
	query_pk_and_slug = True
	action = 'like_toggle'

	def get_queryset(self):
		return Post.objects.published()


class PostDislikeToggleView(ObjectActionToggleView):
	# model = Post
	query_pk_and_slug = True
	action = 'dislike_toggle'

	def get_queryset(self):
		return Post.objects.published()


class CommentLikeToggleView(ObjectActionToggleView):
	model = Comment
	pk_url_kwarg = 'comment_pk'
	action = 'like_toggle'


class CommentDislikeToggleView(ObjectActionToggleView):
	model = Comment
	pk_url_kwarg = 'comment_pk'
	action = 'dislike_toggle'


class CategoryPostListView(PostListView):

	def get_queryset(self):
		category = get_object_or_404(Category, name=self.kwargs['category'])
		return super(CategoryPostListView, self).get_queryset().filter(category=category)
