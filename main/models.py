from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100,null=True)
    username = models.CharField(max_length=100)
    image = models.CharField(max_length=100, null=True)
    banner = models.CharField(max_length=100, null=True)
    bio = models.CharField(max_length=300, null=True)
    profession = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    visibility = models.CharField(max_length=100, choices=[('public', 'Public'), ('private', 'Private')])
    created_date = models.DateTimeField(auto_now_add=True)

class Tracker(models.Model):
    user_id = models.CharField(max_length=100)
    tracked_by = models.CharField(max_length=100)
    conn_code = models.CharField(max_length=100)

class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=100)
    title = models.CharField(max_length=500)
    file = models.CharField(max_length=100, null=True)
    likes_count = models.IntegerField()
    share_count = models.IntegerField()
    uploaded_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(null=True, blank=True)
    type = models.CharField(max_length=100)

class Like(models.Model):
    post_id = models.CharField(max_length=100)
    user_id = models.CharField(max_length=100)

class Comments(models.Model):
    text = models.CharField(max_length=100)
    post_id = models.CharField(max_length=100)
    user_id = models.CharField(max_length=100)

class Article(models.Model):
    article_id = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=100)
    title = models.CharField(max_length=500)
    content = models.TextField(default='')
    file = models.CharField(max_length=100, null=True)
    likes_count = models.IntegerField()
    share_count = models.IntegerField()
    updated_time = models.DateTimeField(null=True, blank=True)
