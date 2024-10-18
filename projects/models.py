import uuid
"""
models.py
This module defines the database models for the fault-finder project.
Classes:
    Project: Represents a project with a title, description, owner, users, and timestamps for creation and updates.
Models:
    Project:
        title (CharField): The title of the project.
        description (TextField): A detailed description of the project.
        owner (ForeignKey): The user who owns the project.
        users (ManyToManyField): The users assigned to the project.
        created_date (DateTimeField): The date and time when the project was created.
        updated_date (DateTimeField): The date and time when the project was last updated.
        updated_by (ForeignKey): The user who last updated the project.
Methods:
    __str__: Returns the string representation of the project, which is its title.
"""
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Project(models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField()
    owner=models.ForeignKey(User, on_delete=models.CASCADE)
    users=models.ManyToManyField(User, related_name='assigned_projects')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='updated_projects', null=True, blank=True)

    def __str__(self):
        return self.title
    
