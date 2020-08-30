from django.db import models
from django.conf import settings
from django.urls import reverse
from PIL import Image
from django.utils.text import slugify
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
	slug = models.SlugField(default='', max_length=120, editable=False)
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

	def save(self, *args, **kwargs):
		self.slug = slugify(self.title, allow_unicode=True)
		super().save(*args, **kwargs)

		img = Image.open(self.thumbnail.path)
		if img.height > 375 or img.width > 500:
			output_size = (500, 375)
        #   extension = img.format.lower()
			img.thumbnail(output_size, Image.ANTIALIAS)
        #   thumbnail.file = type(thumbnail.file)()
			img.save(self.thumbnail.path, quality=100, optimize=True)


		# if img.height > 375 or img.width > 500:
		# 	output_size = (500, 375)
		# 	new_img = img.resize(output_size, Image.ANTIALIAS)
		# 	new_img.save(self.thumbnail.path)

	def get_absolute_url(self):
		return reverse('blog:post_detail', kwargs={'pk': self.pk, 'slug': self.slug})

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
