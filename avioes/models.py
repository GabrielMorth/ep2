from django.db import models
from django.conf import settings

# Create your models here.

class Post(models.Model):
    name = models.CharField("Nome",max_length=255)
    caption = models.CharField("Legenda",max_length=255)
    poster_url = models.URLField("URL do avião",max_length=300, null=True)
    steps_url = models.URLField("URL das instruções",max_length=300, null=True)
    post_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} ({self.post_date})'
    

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    autor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    text = models.CharField("Comentário",max_length=255)
    post_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ["-post_date"]

    def __str__(self):
        return f'{self.autor}: {self.text} ({self.post_date})'

class Category(models.Model):
    name = models.CharField(max_length=255)
    posts = models.ManyToManyField(Post)
    description = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}'