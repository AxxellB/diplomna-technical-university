from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.utils import timezone

class Category(models.Model):
  name = models.CharField(max_length=15, unique=True)
  color = models.CharField(max_length=20, null=True, blank=True)

  def __str__(self):
    return self.name

class Tag(models.Model):
  name = models.CharField(max_length=15, unique=True)
  color = models.CharField(max_length=20, null=True, blank=True)

  def __str__(self):
    return self.name


class Post(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(max_length=2000)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    views = models.IntegerField(blank=True, null=True, default=0)
    replies = models.IntegerField(blank=True, null=True, default=0)
    created_date = models.DateTimeField('date created', default=timezone.now)

    def __str__(self):
        return self.name


class Reply(models.Model):
    text = models.TextField(max_length=1000)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'User: {self.user} - reply: {self.text}'


class Rule(models.Model):
    text = models.TextField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.text
