from django.db import models

# Create your models here.
class Myinfo(models.Model):
    name = models.CharField("名前",max_length=30)
    twitter = models.URLField("Twitter")
    github = models.URLField("GitHub")
    email = models.EmailField("E-mail")
    location = models.CharField("所在地"max_length=50)

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField("タイトル",max_length=100)
    
