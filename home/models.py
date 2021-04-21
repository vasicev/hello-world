from django.db import models
from datetime import datetime

class Tag(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Task(models.Model):
    title = models.CharField(max_length=200)
    tags = models.ManyToManyField(Tag)
    description = models.TextField()
    created = models.DateTimeField(default=datetime.now)
    active = models.BooleanField()

    def __str__(self):
        return self.title
