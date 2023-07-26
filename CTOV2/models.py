from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    mail = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    active = models.IntegerField()

class Department(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    active = models.IntegerField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

class Project(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

class Task(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_by_tasks')
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

class Task_status(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    task_id = models.ForeignKey(Task, on_delete=models.CASCADE)


class TaskComment(models.Model):
    id = models.AutoField(primary_key=True)
    task_id = models.ForeignKey(Task, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField()

class DepartmentsUsers(models.Model):
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

class ProjectsUsers(models.Model):
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

class ProjectsTasks(models.Model):
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    task_id = models.ForeignKey(Task, on_delete=models.CASCADE)
