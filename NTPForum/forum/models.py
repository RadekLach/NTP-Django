from django.db import models
from django.contrib.auth.models import User


class Thread(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, blank=False, null=True)
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=1024)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, blank=False, null=True)
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    text = models.CharField(max_length=1024)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
