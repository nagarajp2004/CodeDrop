from django.db import models
from django.contrib.auth.models import User

class CodeSnippet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class SnippetTracker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    last_sent_index = models.IntegerField(default=-1)
