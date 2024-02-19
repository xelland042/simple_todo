from django.db import models


class BaseClass(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Todo(BaseClass):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} - {self.is_done}'
