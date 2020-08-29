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
	DRAFT = 'dt'
	PUBLISHED = 'pd'

	STATUS_CHOICES = (
		(DRAFT, 'Draft'),
		(PUBLISHED, 'Published')
	)

	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, 
								related_name='posts', related_query_name='post')
	title = models.CharField(max_length=120)
	# content = models.TextField()
	content = HTMLField()
	# slug = models.SlugField()
	status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=DRAFT)
	category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts', 
								related_query_name='post', default=1)
	thumbnail = models.ImageField(default="default_tb.png", upload_to='post_thumbnails')
	likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='post_likes', blank=True)
	dislikes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='post_dislikes', blank=True)
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

	def num_likes(self):
		return self.likes.count()

	def num_dislikes(self):
		return self.dislikes.count()


class Comment(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
							   related_name='comments', related_query_name='comment')
	post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', 
							 related_query_name='comment')
	content = models.TextField()
	likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='comment_likes', blank=True)
	dislikes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='comment_dislikes', blank=True)
	date_created = models.DateField(auto_now_add=True)
	date_updated = models.DateField(auto_now=True)

	class Meta:
		ordering = ['-date_created']

	def num_likes(self):
		return self.likes.count()

	def num_dislikes(self):
		return self.dislikes.count()
