from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Project
from .serializers import ProjectSerializer, CreateProjectSerializer
from rest_framework.decorators import api_view, permission_classes



class UserProjectView(ListAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Project.objects.filter(users=user)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_project(request):
    if request.method == 'POST':
        # Create a mutable dictionary from request.data
        mutable_data = request.data.copy()
        print(mutable_data)

        # Ensure the current user is added to the 'users' field
        mutable_data['users'] = [request.user.id]


        # Set the 'owner' field to the current user
        mutable_data['owner'] = request.user.id



        mutable_data["updated_by"]=request.user.id
        # Continue with the default create logic using the serializer
        serializer = CreateProjectSerializer(data=mutable_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)