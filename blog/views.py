from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from .forms import PostForm
from django.contrib.auth import get_user_model
from django.views.generic import (
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