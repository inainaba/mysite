from django.db import models

""" 自分の情報 """
class Myinfo(models.Model):
    name = models.CharField("名前",max_length=30)
    twitter = models.URLField("Twitter")
    github = models.URLField("GitHub")
    email = models.EmailField("E-mail")
    location = models.CharField("所在地"max_length=50)

    def __str__(self):
        return self.name


""" ミニブログ用 """
class Blog(models.Model):
    title = models.CharField("タイトル",max_length=100)
    date_birth = models.DateField(auto_now_add=True)
    date_update = models.DateField(auto_now=True)
    picture = models.ImageField(upload_to='images/', null=True, blank=True)
    text = models.TextField("本文")
    is_public = models.BooleanField(default=True)
    #tag


""" タグ """
class Tag(models.Model):
    pass



""" ポートフォリオページ用 """
class Work(models.Model):
    pass


""" ジャンル """
class Subject(models.Model):
    pass