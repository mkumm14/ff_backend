from rest_framework.views import APIView
"""
This module defines the view for retrieving bugs associated with a specific project.
Classes:
    BugsByProjectView(APIView): A view that handles GET requests to retrieve bugs for a given project.
Methods:
    BugsByProjectView.get(request, pk): Handles GET requests to retrieve bugs for the project with the specified primary key (pk).
    - Parameters:
        - request: The HTTP request object.
        - pk: The primary key of the project for which to retrieve bugs.
    - Returns:
        - Response: A Response object containing serialized bug data if the project exists.
        - Response: A Response object with HTTP 404 status if the project does not exist.
"""
from rest_framework.response import Response
from rest_framework import status
from .models import Bug
from projects.models import Project
from .serializers import BugSerializer

class BugsByProjectView(APIView):
    def get(self, request, pk):
        try:
            bugs = Bug.objects.filter(project__pk=pk)
            serializer = BugSerializer(bugs, many=True)
            return Response(serializer.data)
        except Project.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        

