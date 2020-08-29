from django.db import models
from django.conf import settings
from django.urls import reverse
from tinymce.models import HTMLField

# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length=25)
	date_added = models.DateField(auto_now_add=True)
	date_updated = models.DateField(auto_now=True)

	class Meta:
		verbose_name_plural = 'Categories'

	def __str__(self):
		return self.name


class Post(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, 
								related_name='posts', related_query_name='post')
	title = models.CharField(max_length=120)
	# content = models.TextField()
	content = HTMLField()
	# slug = models.SlugField()
	category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts', 
								related_query_name='post', default=1)
	thumbnail = models.ImageField(default="default_tb.png", upload_to='post_thumbnails')
	date_published = models.DateField(blank=True, null=True)
	date_created = models.DateField(auto_now_add=True)
	date_updated = models.DateField(auto_now=True)

	class Meta:
		ordering = ['-date_published']

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('blog:post_detail', kwargs={'pk': self.pk})

	def num_comments(self):
		return self.comments.count()


class Comment(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
							   related_name='comments', related_query_name='comment')
	post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', 
							 related_query_name='comment')
	content = models.TextField()
	date_created = models.DateField(auto_now_add=True)
	date_updated = models.DateField(auto_now=True)

	class Meta:
		ordering = ['-date_created']
