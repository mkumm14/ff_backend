from rest_framework import permissions

from rest_framework.permissions import BasePermission

def is_owner_or_read_only(request, project):
    """
    Custom permission to allow owners of a project to edit it.
    """
    if request.method in permissions.SAFE_METHODS:
        return True  # Allow safe methods (GET, HEAD, OPTIONS)

    # Check if the user making the request is the owner of the project
    return project.owner == request.user


class IsUserOfProject(BasePermission):
    """
    Custom permission to only allow owners of an object to access it.
    """

    def has_object_permission(self, request, view, obj):
        # Assuming the model instance has an `owner` attribute.
        return obj.users.filter(id=request.user.id).exists()
