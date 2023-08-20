from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Project
from .serializers import ProjectSerializer

class UserProjectView(ListAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Project.objects.filter(users=user)
