from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_premium = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class Article(models.Model):
    title = models.CharField(max_length=256)
    text = models.TextField()
    is_paid = models.BooleanField()

    def __str__(self):
        return self.title
