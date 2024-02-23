# Create your models here.
# blog/models.py
from django.db import models
from django.urls import reverse_lazy

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
            "accounts.CustomUser",
            on_delete=models.CASCADE,
        )
    body = models.TextField()
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse_lazy("post_detail", kwargs={"pk": self.pk})
    