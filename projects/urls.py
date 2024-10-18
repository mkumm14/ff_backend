from django.urls import path, include
"""
URL configuration for the projects app.
This module defines the URL patterns for the projects-related views in the application.
Routes:
    - 'user-projects': Maps to UserProjectView for displaying user-specific projects.
    - 'create': Maps to create_project view for creating a new project.
    - 'update/<int:pk>': Maps to update_project view for updating an existing project identified by its primary key (pk).
    - '<int:pk>': Maps to ProjectDetailsView for displaying details of a specific project identified by its primary key (pk).
    - 'delete/<int:pk>': Maps to delete_project view for deleting a specific project identified by its primary key (pk).
Imports:
    - path: Function to define URL patterns.
    - include: Function to include other URL configurations.
    - views: Module containing the view functions and classes for the projects app.
"""
from . import views

urlpatterns = [
    path('user-projects', views.UserProjectView.as_view(), name='user-projects'),
    path('create', views.create_project, name="create-project"),
    path('update/<int:pk>', views.update_project, name='update-project'),
    path('<int:pk>', views.ProjectDetailsView.as_view(), name="project-details"),
    path('delete/<int:pk>', views.delete_project, name='delete-project'),
]

