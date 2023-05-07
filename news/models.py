from django.db import models
from django.utils import timezone


class Event(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    file = models.FileField(upload_to="media/")
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish']),
        ]

    def __str__(self):
        return self.title
