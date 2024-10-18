from django.urls import path, include
"""
URL configuration for the bugs module.
This module defines the URL patterns for the bugs-related views in the application.
Routes:
    - <int:pk>/project-bugs: Maps to the BugsByProjectView, which displays bugs for a specific project.
Imports:
    - path: Function to define URL patterns.
    - include: Function to include other URL configurations.
    - BugsByProjectView: View to handle displaying bugs by project.
Attributes:
    urlpatterns (list): List of URL patterns for the bugs module.
"""
from .views import BugsByProjectView

urlpatterns = [
    path("<int:pk>/project-bugs", BugsByProjectView.as_view(), name='project_bugs')
]

