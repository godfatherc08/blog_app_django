from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.TextField(max_length=200, null=False)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

