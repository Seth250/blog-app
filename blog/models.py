from django.db import models
from django.conf import settings
from django.urls import reverse
from PIL import Image
from django.utils.text import slugify
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
import readtime

# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length=25)
	date_added = models.DateField(auto_now_add=True)
	date_updated = models.DateField(auto_now=True)

	class Meta:
		verbose_name_plural = 'Categories'

	def __str__(self):
		return self.name


class PostQuerySet(models.QuerySet):

	def published(self):
		return self.filter(status='pd').order_by('-date_published')

	def drafted(self):
		return self.filter(status='dt').order_by('-date_updated')


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
	content = models.TextField(blank=True, null=True) # because of tinymce validation errors, maybe try only blank
	slug = models.SlugField(max_length=120, default='', editable=False)
	read_time = models.CharField(max_length=25, default='', editable=False)
	status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=DRAFT)
	category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts', 
								related_query_name='post', default=1)
	thumbnail = models.ImageField(default="default_tb.png", upload_to='post_thumbnails')
	likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='post_likes', blank=True)
	dislikes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='post_dislikes', blank=True)
	objects = PostQuerySet.as_manager() 
	date_published = models.DateTimeField(null=True, editable=False)
	date_created = models.DateTimeField(auto_now_add=True)
	date_updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		self.slug = slugify(self.title, allow_unicode=True)
		self.read_time = readtime.of_text(self.content)
		super().save(*args, **kwargs)

		img = Image.open(self.thumbnail.path)
		if img.width > 640 or img.height > 640:
			output_size = (640, 640)
			img.thumbnail(output_size, Image.ANTIALIAS)
			img.save(self.thumbnail.path, optimize=True)

	def get_absolute_url(self):
		return reverse('blog:post_detail', kwargs={'pk': self.pk, 'slug': self.slug})

	def publish(self):
		self.status = self.PUBLISHED
		self.date_published = timezone.now()
		self.save()

	def get_num_comments(self):
		return self.comments.count()

	def get_num_likes(self):
		return self.likes.count()

	def get_num_dislikes(self):
		return self.dislikes.count()


class Comment(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
							   related_name='comments', related_query_name='comment')
	post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', 
							 related_query_name='comment')
	content = models.TextField(_('Leave a Comment'))
	likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='comment_likes', blank=True)
	dislikes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='comment_dislikes', blank=True)
	date_created = models.DateField(auto_now_add=True)
	date_updated = models.DateField(auto_now=True)

	class Meta:
		ordering = ['-date_created']

	def get_num_likes(self):
		return self.likes.count()

	def get_num_dislikes(self):
		return self.dislikes.count()
