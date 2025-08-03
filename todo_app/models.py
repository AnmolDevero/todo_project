from django.db import models
# Create your models here.

from django.utils import timezone
from django.contrib.auth.models import User


# ToDo model
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    is_completed = models.BooleanField(default=False)
    created_at   = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # null=True: Allows this field to be empty in the database.
    # blank=True: Allows this field to be empty in forms (no validation error).
    due_date = models.DateField(null=True,blank=True) 
    # Links each task to a user.
    # Ensures only the associated user can view/edit their own tasks (handled in views).
    # Not shown in form; handled through backend logic.
    user    = models.ForeignKey(User, on_delete=models.CASCADE, null=True) 

    def __str__(self):
        return self.title # Shows the task's title instead of "Task object" in the admin panel.