# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Article(models.Model):

    title = models.CharField(max_length=150)
    url = models.URLField(null=True)
    text = models.TextField()
    small_text = models.CharField(max_length=300)
    author = models.ForeignKey(User, related_name='articles')
    creation_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now=True)
    publication_date = models.DateTimeField()
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.title



