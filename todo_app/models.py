from django.db import models
# Create your models here.
from django.contrib.auth.models import User


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    is_completed = models.BooleanField(default=False)
    created_at   = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    due_date = models.DateField(null=True,blank=True) 
    user    = models.ForeignKey(User, on_delete=models.CASCADE) 

    def __str__(self):
        return self.title 