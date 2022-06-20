from datetime import datetime
from tkinter import CASCADE
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Post(models.Model):
  title = models.CharField(max_length=255)
  text =  models.TextField(max_length=100)
  author = models.ForeignKey(
      get_user_model(), 
      on_delete=models.CASCADE)
  Created_date = models.DateTimeField(datetime.now())
  Published_date = models.DateTimeField(datetime.now())
  def __str__(self):
        return self.title