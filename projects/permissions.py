from rest_framework import permissions

def is_owner_or_read_only(request, project):
    """
    Custom permission to allow owners of a project to edit it.
    """
    if request.method in permissions.SAFE_METHODS:
        return True  # Allow safe methods (GET, HEAD, OPTIONS)

    # Check if the user making the request is the owner of the project
    return project.owner == request.user
