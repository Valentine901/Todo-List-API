from django.db import models
from user.models import User 

class TodoList(models.Model):
    title = models.CharField(max_length=100, null=False)
    description = models.TextField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    mark_completed = models.BooleanField(default=False)


    class Meta:
        ordering = ["-updated_at"]