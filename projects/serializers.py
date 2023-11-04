from rest_framework import serializers
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
