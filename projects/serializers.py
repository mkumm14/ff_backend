from rest_framework import serializers
"""
This module contains serializers for the Project model, which are used to convert model instances to JSON and vice versa.
Classes:
    ProjectSerializer: A serializer for the Project model that includes fields for the owner and the user who last updated the project.
    CreateProjectSerializer: A serializer for creating new Project instances.
    UpdateProjectSerializer: A serializer for updating existing Project instances.
    ProjectDetailsSerializer: A serializer for detailed representation of the Project model, including related user information.
Classes:
    ProjectSerializer:
        - owner: Read-only field representing the username of the project's owner.
        - updated_by: Read-only field representing the username of the user who last updated the project.
        - Meta: Metadata for the serializer, specifying the model and fields to include.
    CreateProjectSerializer:
        - Meta: Metadata for the serializer, specifying the model and fields to include for creating a project.
    UpdateProjectSerializer:
        - Meta: Metadata for the serializer, specifying the model and fields to include for updating a project.
    ProjectDetailsSerializer:
        - owner_username: Read-only field representing the username of the project's owner.
        - users: Read-only field representing the usernames of users associated with the project.
        - updated_by_username: Read-only field representing the username of the user who last updated the project.
        - Meta: Metadata for the serializer, specifying the model and fields to include for detailed project representation.
"""
from django.contrib.auth.models import User
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    owner = serializers.CharField(source='owner.username', read_only=True)
    updated_by = serializers.CharField(source='updated_by.username', read_only=True, allow_null=True)

    class Meta:
        model = Project
        fields = ['id', 'title', 'owner', 'created_date', 'updated_date', 'updated_by']



class CreateProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields=['id','title','description','users','updated_by','owner']


class UpdateProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=Project
        fields=['title', 'description', 'updated_by']



class ProjectDetailsSerializer(serializers.ModelSerializer):
    owner_username = serializers.ReadOnlyField(source='owner.username')
    users = serializers.SlugRelatedField(
        many=True,
        slug_field='username',
        read_only=True
     )
    updated_by_username = serializers.ReadOnlyField(source='updated_by.username')

    class Meta:
        model = Project
        fields = [
            'id', 'title', 'description', 'users', 
            'created_date', 'updated_date',
            'owner_username', 'updated_by_username'
        ]
        read_only_fields = ('id',)  # You can make 'id' read-only if you don't want it to be editable

    # If you need to perform complex data presentation you can define methods here





