from django.db import models
"""
This module defines the models for the bug tracking system.
Classes:
    Bug: A model representing a bug in the system.
Bug Model:
    Fields:
        title (CharField): The title of the bug.
        description (TextField): A detailed description of the bug.
        status (CharField): The current status of the bug. Choices are 'new', 'in_progress', 'fixed', 'closed'. Default is 'new'.
        priority (CharField): The priority level of the bug. Choices are 'low', 'medium', 'high'. Default is 'medium'.
        reporter (ForeignKey): The user who reported the bug. Linked to the User model.
        assigned_to (ManyToManyField): The users assigned to fix the bug. Linked to the User model.
        project (ForeignKey): The project to which the bug belongs. Linked to the Project model.
        image (ImageField): An optional image related to the bug. Uploaded to 'bug_images/'.
        created_date (DateTimeField): The date and time when the bug was created. Automatically set on creation.
        updated_date (DateTimeField): The date and time when the bug was last updated. Automatically set on update.
        updated_by (ForeignKey): The user who last updated the bug. Linked to the User model. Can be null.
    Methods:
        __str__: Returns the string representation of the bug, which is its title.
"""
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
    

