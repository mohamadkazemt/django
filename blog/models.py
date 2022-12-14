from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from datetime import datetime
# from django.db.models.fields.files import FieldFile


# def validate_file_extension(value):
#   import os
#   from django.core.exceptions import ValidationError
#   ext = os.path.splitext(value.name)[1]
#   valid_extensions = ['.jpg', '.png']
#   if not ext.lower() in valid_extensions:
#   raise ValidationError('Unsupported file extension.')


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='files/user_avatar/', null=False, blank=False)
    description = models.CharField(max_length=512, null=False, blank=False)


class Article(models.Model):
    title = models.CharField(max_length=128, null=False, blank=False)
    cover = models.ImageField(upload_to='files/article_cover/', null=False, blank=False)
    content = RichTextField()
    created_at = models.DateTimeField(default=datetime.now, blank=False)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    author = models.OneToOneField(UserProfile, on_delete=models.CASCADE)


class Category(models.Model):
    title = models.CharField(max_length=128, null=False, blank=False)
    cover = models.ImageField(upload_to='files/category_cover/', null=False, blank=False)

