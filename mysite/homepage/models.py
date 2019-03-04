from django.db import models

from stdimage.models import StdImageField 

""" 自分の情報 """
class Myinfo(models.Model):
    name = models.CharField("名前",max_length=30)
    twitter = models.URLField("Twitter",null=True, blank=True)
    github = models.URLField("GitHub",null=True, blank=True)
    facebook = models.URLField("Facebook",null=True, blank=True)
    email = models.EmailField("E-mail",null=True, blank=True)
    location = models.CharField("所在地",max_length=50)
    selling_point = models.CharField("アピールポイント",max_length=500)
    detail = models.TextField("いままで", null=True, blank=True)
    picture = StdImageField("画像",upload_to='static/homepage/myinfos', blank=True, variations={
        'large': (600, 400),
        'thumbnail': (100, 100, True),
        'medium': (300, 200),
    })

    def __str__(self):
        return self.name


""" ミニブログ用 """
class Blog(models.Model):
    title = models.CharField("タイトル",max_length=100)
    text = models.TextField("本文")
    is_public = models.BooleanField(default=True)
    date_birth = models.DateField(auto_now_add=True)
    date_update = models.DateField(auto_now=True)
    picture = StdImageField("画像",upload_to='static/homepage/blogs', blank=True, variations={
        'large': (600, 400),
        'thumbnail': (100, 100, True),
        'medium': (300, 200),
    })

    def __str__(self):
        return self.title


""" ジャンル """
class Subject(models.Model):
    name = models.CharField("ジャンル名",max_length=100)

    def __str__(self):
        return self.name


""" ポートフォリオページ用 """
class Work(models.Model):
    title = models.CharField("webアプリ名",max_length=100)
    text = models.TextField("説明")
    page = models.URLField("URL")
    is_public = models.BooleanField(default=True)
    date_birth = models.DateField(auto_now_add=True)
    date_update = models.DateField(auto_now=True)
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    picture = StdImageField("画像",upload_to='static/homepage/works', blank=True, variations={
        'large': (600, 400),
        'thumbnail': (100, 100, True),
        'medium': (300, 200),
    })

    def __str__(self):
        return self.title
