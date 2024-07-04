from django.contrib import admin

# Register your models here.
from forum_main.models import Post, Reply, Rule

admin.site.register(Post)
admin.site.register(Reply)
admin.site.register(Rule)