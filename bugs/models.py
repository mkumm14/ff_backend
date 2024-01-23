from django.db import models
from django.contrib.auth.models import User
from projects.models import Project
# Create your models here.



class Bug(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=[('new', 'New'), ('in_progress', 'In Progress'), ('fixed', 'Fixed'), ('closed', 'Closed')], default='new')
    priority = models.CharField(max_length=20, choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')], default='medium')
    reporter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reported_bugs')
    assigned_to = models.ManyToManyField(User, related_name='assigned_bugs', blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='bugs')
    image = models.ImageField(upload_to='bug_images/', blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='updated_bugs', null=True, blank=True)

    def __str__(self):
        return self.title