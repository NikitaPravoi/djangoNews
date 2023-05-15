from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User



class User(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset() \
            .filter(status=Event.Status.PUBLISHED)


class Event(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Черновик'
        PUBLISHED = 'PB', 'Опубликован'

    title = models.CharField(max_length=250)
    body = models.TextField()
    participants = models.ManyToManyField(User)
    file = models.FileField(upload_to="media/", null=True, blank=True)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    event_date = models.DateTimeField(default=timezone.now)

    objects = models.Manager()

    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish']),
        ]

    def __str__(self):
        return self.title
