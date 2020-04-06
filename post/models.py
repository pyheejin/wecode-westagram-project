from django.db import models

# Create your models here.
from user.models import User


class Comment(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    text = models.CharField(max_length=300)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name