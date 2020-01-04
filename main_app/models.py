from django.db import models
from django.urls import reverse
# Create your models here.

class Todo(models.Model):
    todo_item = models.CharField(max_length=100, default=None)
    def __str__(self):
        return f"{self.todo_item}"
    def get_absolute_url(self):
        return reverse('todos_detail', kwargs={'pk': self.id})


        