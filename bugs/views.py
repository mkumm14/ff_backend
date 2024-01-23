from rest_framework.views import APIView
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