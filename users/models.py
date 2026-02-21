from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.db.models.signals import post_save
from django.dispatch import receiver
import os


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    image = models.ImageField(
        default='profile_pics/default.png',
        upload_to='profile_pics',
    )

    favorite_game = models.CharField(max_length=100, blank=True)
    twitter = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # Resize only for local filesystems that expose a real file path.
        try:
            image_path = self.image.path
        except (ValueError, NotImplementedError):
            image_path = None

        if self.image and image_path and os.path.exists(image_path):
            img = Image.open(image_path)
            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(image_path)


# Signals to automatically create and save profiles
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
