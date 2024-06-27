from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.utils import timezone

category_choices = [
    ('HOBBIES', 'Hobbies'),
    ('VIDEO', 'Video'),
    ('ARTS', 'Arts'),
    ('GAMING', 'Gaming'),
    ('EXCHANGE', 'Exchange'),
    ('ENTERTAINMENT', 'Entertainment'),
    ('SOCIAL', 'Social'),
    ('RANDOM', 'Random'),
    ('TECH', 'Tech'),
    ('SCIENCE', 'Science'),
    ('Q&As', 'Q&As'),
    ('PETS', 'Pets'),
    ('EDUCATION', 'Education'),
    ('POLITICS', 'Politics'),
]
tags_choices = [
    ('GAMING', 'Gaming'),
    ('NATURE', 'Nature'),
    ('ENTERTAINMENT', 'Entertainment'),
    ('SELFIE', 'Selfie'),
    ('CAMERA', 'Camera'),
    ('USERNAME', 'Username'),
    ('FUNNY', 'Funny'),
    ('PHOTOGRAPHY', 'Photography'),
    ('CLIMBING', 'Climbing'),
    ('ADVENTURE', 'Adventure'),
    ('DREAMS', 'Dreams'),
    ('LIFE', 'Life'),
    ('REASON', 'Reason'),
    ('SOCIAL', 'Social'),
]
is_mature_choices = [('Yes', 'Yes'), ('No', 'No')]


class Post(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=20000)
    category = models.CharField(max_length=15, choices=category_choices, default='Hobbies')
    tag = models.CharField(max_length=15, choices=tags_choices, default='Gaming')
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    views = models.IntegerField(blank=True, null=True, default=0)
    replies = models.IntegerField(blank=True, null=True, default=0)
    tag_color = models.CharField(max_length=20, null=True, blank=True)
    category_color = models.CharField(max_length=20, null=True, blank=True)
    created_date = models.DateTimeField('date created', default=timezone.now)

    def __str__(self):
        return self.name


class Reply(models.Model):
    text = models.TextField(max_length=10000)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'User: {self.user} - reply: {self.text}'


class Rules(models.Model):
    text = models.TextField(max_length=5000)

    def __str__(self):
        return self.text
