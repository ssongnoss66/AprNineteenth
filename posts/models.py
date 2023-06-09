from django.db import models
from django.conf import settings

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    select1_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='select1_post')
    select1_content = models.CharField(max_length=50)
    select2_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='select2_post')
    select2_content = models.CharField(max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)