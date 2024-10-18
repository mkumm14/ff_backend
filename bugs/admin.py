from django.contrib import admin
"""
This module registers the Bug model with the Django admin site.
Imports:
    from django.contrib import admin: Imports the Django admin module.
    from bugs.models import Bug: Imports the Bug model from the bugs application.
Functionality:
    Registers the Bug model with the Django admin site to enable management of Bug instances through the admin interface.
"""

from bugs.models import Bug

# Register your models here.


admin.site.register(Bug)


