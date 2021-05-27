from django.db import models

# Create your models here.
class Post(models.Model):
    name = models.CharField("제목", max_length=31)
    image = models.ImageField("이미지")
