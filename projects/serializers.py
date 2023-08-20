from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    owner = serializers.CharField(source='owner.username', read_only=True)
    updated_by = serializers.CharField(source='updated_by.username', read_only=True, allow_null=True)

    class Meta:
        model = Project
        fields = ['id', 'title', 'owner', 'created_date', 'updated_date', 'updated_by']
