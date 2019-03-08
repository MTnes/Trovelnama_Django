from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Team_Members(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    url_Facebook=models.URLField()
    url_Gmail=models.URLField()
    url_Linkedin=models.URLField()
    url_Twitter=models.URLField()
    designation = models.CharField(max_length=100)
    image = models.ImageField(blank=True, null=True, upload_to='images/')
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'team_members'
        verbose_name_plural = 'Team_Members'
    def __self__(self):
        return self.name

class Blogs(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    url = models.URLField()
    icon_Class_Name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'blogs'
        verbose_name_plural = 'Blogs'
    def __self__(self):
        return self.name

class Messages(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'messages'
        verbose_name_plural = 'Messages'
    def __self__(self):
        return self.name


