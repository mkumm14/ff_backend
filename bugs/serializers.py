from rest_framework import serializers
"""
This module contains the serializer for the Bug model.
Classes:
    BugSerializer: A serializer for the Bug model, which includes all fields by default.
Usage:
    This serializer can be used to convert Bug model instances to JSON and vice versa.
"""
from .models import Bug

class BugSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bug
        fields = '__all__'  # Adjust fields as necessary
