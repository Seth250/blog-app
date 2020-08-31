from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
	date_of_birth = models.DateField(blank=True, null=True)
	profile_image = models.ImageField(default='default_pp.png', upload_to='profile_pictures')

	def __str__(self):
		return self.username