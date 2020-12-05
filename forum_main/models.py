from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.TextField()


class Section(models.Model):
    name = models.TextField()
    description = models.TextField()
    section = models.ForeignKey(Category, on_delete=models.CASCADE)