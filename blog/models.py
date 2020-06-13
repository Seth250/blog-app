from django.db import models
from django.conf import settings
from django.urls import reverse

# Create your models here.


class Post(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, 
								related_name='posts', related_query_name='post')
	title = models.CharField(max_length=100)
	content = models.TextField()
	date_posted = models.DateField(auto_now_add=True)
	date_updated = models.DateField(auto_now=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('blog:post_detail', kwargs={'pk': self.pk})


class Comment(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
							   related_name='comments', related_query_name='comment')
	post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', 
							 related_query_name='comment')
	content = models.TextField()
	date_posted = models.DateField(auto_now_add=True)
	date_updated = models.DateField(auto_now=True)