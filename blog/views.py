from django.shortcuts import render
from .models import Post
from .forms import PostForm
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