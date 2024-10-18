from django.contrib import admin
"""
This module registers the Project model with the Django admin site.
Imports:
    from django.contrib import admin: Imports the Django admin module.
    from projects.models import Project: Imports the Project model from the projects app.
Functionality:
    Registers the Project model with the Django admin site, allowing it to be managed through the admin interface.
"""

from projects.models import Project

# Register your models here.


admin.site.register(Project)

