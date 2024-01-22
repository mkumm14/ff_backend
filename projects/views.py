from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Project
from .serializers import (
    ProjectDetailsSerializer,
    ProjectSerializer,
    CreateProjectSerializer,
    UpdateProjectSerializer,
)
from rest_framework.decorators import api_view, permission_classes
from .permissions import is_owner_or_read_only, IsUserOfProject


class UserProjectView(ListAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Project.objects.filter(users=user)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_project(request):
    if request.method == "POST":
        # Create a mutable dictionary from request.data
        mutable_data = request.data.copy()
        print(mutable_data)

        # Ensure the current user is added to the 'users' field
        mutable_data["users"] = [request.user.id]

        # Set the 'owner' field to the current user
        mutable_data["owner"] = request.user.id

        mutable_data["updated_by"] = request.user.id
        # Continue with the default create logic using the serializer
        serializer = CreateProjectSerializer(data=mutable_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["PUT", "PATCH"])
@permission_classes([IsAuthenticated])
def update_project(request, pk):
    try:
        project = Project.objects.get(pk=pk)
    except Project.DoesNotExist:
        return Response(
            {"error": "Project not found"}, status=status.HTTP_404_NOT_FOUND
        )

    if not is_owner_or_read_only(request, project):
        return Response(
            {"error": "You do not have permission to update this project"},
            status=status.HTTP_403_FORBIDDEN,
        )

    if request.method == "PUT":
        # If it's a PUT request, update all fields
        serializer = UpdateProjectSerializer(project, data=request.data)
    elif request.method == "PATCH":
        # If it's a PATCH request, update only the provided fields
        serializer = UpdateProjectSerializer(project, data=request.data, partial=True)

    if serializer.is_valid():
        # Automatically set the 'updated_by' field to the current user
        serializer.validated_data["updated_by"] = request.user

        # Save the updated project
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ProjectDetailsView(RetrieveAPIView):
    queryset=Project.objects.all()
    serializer_class=ProjectDetailsSerializer
    permission_classes = [IsAuthenticated, IsUserOfProject]

    def get_object(self):
        obj = super().get_object()
        self.check_object_permissions(self.request, obj)
        return obj


    
    
