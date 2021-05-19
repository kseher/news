from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    def __str__(self):
        return f'{self.id}: {self.username}'


class Kommentar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.CharField(max_length=280)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Post by {self.user.username}'

    def serialize(self):
        return {
            'user': self.user.username,
            'post': self.post,
            'timestamp': self.timestamp
        }
