from django.db import models
from django.conf import settings
from PIL import Image

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    image = models.ImageField(default='default_pp.png', upload_to='profile_pictures')
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.user}'s Profile"

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)
        if img.height > 150 or img.width > 150:
            output_size = (150, 150)
            # extension = img.format.lower()
            img = img.resize(output_size, Image.LANCZOS)
            # profile_image.file = type(profile_image.file)()
            # img.save(profile_image.file, extension, optimize=True)
            img.save(self.image.path, optimize=True)

	# 	# return profile_image
