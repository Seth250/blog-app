from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import PostForm
from django.contrib.auth import get_user_model
from django.views.generic import (
	View,
	ListView,
	DetailView,
	CreateView,
	UpdateView,
	DeleteView,
)

# Create your views here.


class PostListView(ListView):
	model = Post
	paginate_by = 2


class UserPostListView(ListView):
	paginate_by = 2

	def get_queryset(self):
		user = get_object_or_404(get_user_model(), username=self.kwargs.get('username'))
		return user.posts.all()


class PostDetailView(DetailView):
	model = Post


class PostCreateView(CreateView):
	model = Post
	form_class = PostForm

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)


class PostUpdateView(UpdateView):
	model = Post
	form_class = PostForm

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)


class ObjectLikeToggleView(View):

	def get(self, request, *args, **kwargs):
		if request.user in self.obj.likes.all():
			self.obj.likes.remove(request.user)

		elif request.user in self.obj.dislikes.all():
			self.obj.dislikes.remove(request.user)
			self.obj.likes.add(request.user)

		else:
			self.obj.likes.add(request.user)

		return redirect('blog:post_detail', pk=self.pk)


class ObjectDislikeToggleView(View):

	def get(self, request, *args, **kwargs):
		if request.user in self.obj.dislikes.all():
			self.obj.dislikes.remove(request.user)

		elif request.user in self.obj.likes.all():
			self.obj.likes.remove(request.user)
			self.obj.dislikes.add(request.user)

		else:
			self.obj.dislikes.add(request.user)

		return redirect('blog:post_detail', pk=self.pk)


class UserPostLikeToggleView(ObjectLikeToggleView):

	def get(self, request, *args, **kwargs):
		self.pk = self.kwargs.get('pk')
		self.obj = get_object_or_404(Post, pk=self.pk)
		return super(UserPostLikeToggleView, self).get(request, *args, **kwargs)


# you can reduce this even further 
class UserPostDislikeToggleView(ObjectDislikeToggleView):

	def get(self, request, *args, **kwargs):
		self.pk = self.kwargs.get('pk')
		self.obj = get_object_or_404(Post, pk=self.pk)
		return super(UserPostDislikeToggleView, self).get(request, *args, **kwargs)
