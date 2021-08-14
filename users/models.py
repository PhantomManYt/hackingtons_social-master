from django.db import models
from django.db.models.signals import post_save
from account.models import CustomUser
from django.dispatch import receiver
from PIL import Image
class Profile(models.Model):
    user = models.OneToOneField(CustomUser, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=50)
    image = models.ImageField(default='default.jpg.jpg', upload_to='profile_pics')
    bio = models.TextField(null=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    #def save(self, *args, **kwargs):
        #super().save(*args, **kwargs)

        #img = Image.open(self.image.path)

        #if img.height > 300 or img.width > 300:
        #    output_size = (300, 300)
         #   img.thumbnail(output_size)
          #  img.save(self.image.path)


