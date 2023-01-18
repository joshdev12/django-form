from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=50)
    desc = models.TextField(blank=True, null=True)
    is_complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title

    