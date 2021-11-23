from django.db import models
from django.db.models.deletion import CASCADE
from django.urls import reverse

# Create your models here.
class BlogThread(models.Model):
    name = models.CharField(max_length=150, unique=True)
    def __str__(self) -> str:
        return self.name

class BlogPost(models.Model):
    title = models.CharField(max_length=250)
    blog_content = models.TextField(max_length=4000)
    blog_thread = models.ForeignKey(BlogThread, on_delete=CASCADE)

    def get_absolute_url(self):
        return reverse("blog_details", kwargs={"id": self.pk})

    def __str__(self) -> str:
        return self.title