from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


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

    def all_participants(self):
        return ", ".join([str(p) for p in self.participants.all()])

    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish']),
        ]

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()

    def __str__(self):
        return self.title


class Work(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    participants = models.ManyToManyField(User, related_name='works_participated')
    # author = models.ForeignKey(User, related_name='works_authored', on_delete=models.CASCADE)
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField()
    project = models.ForeignKey(Project, null=True, on_delete=models.PROTECT)
    plan = models.BooleanField(default=False)
    fact = models.BooleanField(default=False)

    objects = models.Manager()

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    file = models.FileField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish']),
        ]

    def __str__(self):
        return self.title


class Message(models.Model):
    theme = models.CharField(max_length=512,
                             verbose_name='Тема сообщения')

    text = models.CharField(max_length=5000,
                            verbose_name='Текст сообщения')

    date_message = models.DateTimeField(default=timezone.now, blank=True,
                                        verbose_name='Время создания сообщения')

    class Meta:
        ordering = ['-date_message']
        indexes = [
            models.Index(fields=['-date_message']),
        ]

    def __str__(self):
        return self.theme
