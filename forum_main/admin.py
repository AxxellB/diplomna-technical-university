from django.contrib import admin

# Register your models here.
from forum_main.models import Post, Reply

admin.site.register(Post)
admin.site.register(Reply)