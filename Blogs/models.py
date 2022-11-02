from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Blog(models.Model):
    title = models.TextField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.title
