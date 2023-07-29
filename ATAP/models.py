from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User

class Teams(models.Model):

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)

class Projects(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

class Tasks(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)
    project_id = models.ForeignKey(Projects, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks_created_by')
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

class Comments(models.Model):
    id = models.AutoField(primary_key=True)
    comment_type = models.CharField(max_length=255)
    related_id = models.IntegerField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField()