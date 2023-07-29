# Generated by Django 4.2.3 on 2023-07-29 22:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CTOV2', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('comment_type', models.CharField(max_length=255)),
                ('related_id', models.IntegerField()),
                ('comment', models.TextField()),
                ('created_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('active', models.IntegerField()),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('status', models.CharField(max_length=255)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('status', models.CharField(max_length=255)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=255)),
                ('role', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('active', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='departmentsusers',
            name='department_id',
        ),
        migrations.RemoveField(
            model_name='departmentsusers',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='project',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='projectstasks',
            name='project_id',
        ),
        migrations.RemoveField(
            model_name='projectstasks',
            name='task_id',
        ),
        migrations.RemoveField(
            model_name='projectsusers',
            name='project_id',
        ),
        migrations.RemoveField(
            model_name='projectsusers',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='task',
            name='assigned_to',
        ),
        migrations.RemoveField(
            model_name='task',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='task',
            name='project_id',
        ),
        migrations.RemoveField(
            model_name='task_status',
            name='task_id',
        ),
        migrations.RemoveField(
            model_name='taskcomment',
            name='task_id',
        ),
        migrations.RemoveField(
            model_name='taskcomment',
            name='user_id',
        ),
        migrations.DeleteModel(
            name='Department',
        ),
        migrations.DeleteModel(
            name='DepartmentsUsers',
        ),
        migrations.DeleteModel(
            name='Project',
        ),
        migrations.DeleteModel(
            name='ProjectsTasks',
        ),
        migrations.DeleteModel(
            name='ProjectsUsers',
        ),
        migrations.DeleteModel(
            name='Task',
        ),
        migrations.DeleteModel(
            name='Task_status',
        ),
        migrations.DeleteModel(
            name='TaskComment',
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='tasks',
            name='assigned_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CTOV2.users'),
        ),
        migrations.AddField(
            model_name='tasks',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks_created_by', to='CTOV2.users'),
        ),
        migrations.AddField(
            model_name='tasks',
            name='project_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CTOV2.projects'),
        ),
        migrations.AddField(
            model_name='projects',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CTOV2.users'),
        ),
        migrations.AddField(
            model_name='departments',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CTOV2.users'),
        ),
        migrations.AddField(
            model_name='comments',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CTOV2.users'),
        ),
    ]