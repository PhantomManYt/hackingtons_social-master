from django.contrib import admin
from .models import Post, Follow, Announce

admin.site.register(Post)
admin.site.register(Follow)
admin.site.register(Announce)