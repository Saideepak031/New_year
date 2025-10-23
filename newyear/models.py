from django.db import models
from django.utils import timezone

class Wish(models.Model):
    text = models.CharField(max_length=250)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text

class Note(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class Goal(models.Model):
    text = models.CharField(max_length=200)
    is_done = models.BooleanField(default=False)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.text} ({'done' if self.is_done else 'open'})"