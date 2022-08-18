from pyexpat import model
from turtle import update
from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(null=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.title)