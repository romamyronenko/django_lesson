from django.db import models


# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    is_done = models.BooleanField()

    def __str__(self):
        return f'[{self.id}] {self.title} | {self.description}'