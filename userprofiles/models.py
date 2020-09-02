from django.db import models
from django.conf import settings

# Create your models here.

class Profile(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(default='default_pp.png', upload_to='profile_pictures')
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.user}'s Profile"
