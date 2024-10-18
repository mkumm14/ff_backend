from django.urls import path
"""
URL configuration for the users app.
This module defines the URL patterns for the users app, mapping the root URL
to the `UserListView` view.
Routes:
    - '' : Maps to `UserListView` and is named 'user-list'.
Imports:
    - path: Function to define URL patterns.
    - UserListView: View to handle the user list display.
Usage:
    Include this URL configuration in the project's main URL configuration
    to enable the user list view.
"""
from .views import UserListView

urlpatterns = [
    path('', UserListView.as_view(), name='user-list'),
]