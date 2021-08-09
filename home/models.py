from django.db import models
from django.db.models.deletion import CASCADE
from django.utils import timezone
from account.models import CustomUser
from django.urls import reverse
import uuid

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(null=True, blank=True, upload_to="images")
    link = models.URLField(max_length=500, blank=True)
    link_title = models.CharField(max_length=100, blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    likes = models.ManyToManyField(CustomUser, related_name='likes')    
    dislikes = models.ManyToManyField(CustomUser, related_name='dislikes')

    def total_likes(self):
        return self.likes.count()

    def total_dislikes(self):
        return self.dislikes.count()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE, null=True)
    content = models.TextField()
    link = models.URLField(max_length=500, blank=True)
    link_title = models.CharField(max_length=100, blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)

class Follow(models.Model):
    user_from = models.ForeignKey(CustomUser, related_name='rel_from_set', on_delete=models.CASCADE)
    user_to = models.ForeignKey(CustomUser, related_name='rel_to_set', on_delete=models.CASCADE) 
    create = models.DateTimeField(auto_now_add=True, db_index=True)


    def __str__(self):
        return '{} follows {}'.format(self.user_from, self.user_to)

class Announce(models.Model):
    announcement = models.TextField()
    person = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse('announcements')

class UserList(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=CASCADE)



CustomUser.add_to_class('following', models.ManyToManyField('self', through=Follow, related_name='followers', symmetrical=False))

