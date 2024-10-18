from django.shortcuts import render
"""
This module contains views related to user operations.
Classes:
    UserListView: A view that provides a read-only endpoint to list all users.
Imports:
    render: Renders a template with a context.
    User: The user model provided by Django's authentication system.
    generics: Provides generic class-based views for Django REST framework.
    UserSerializer: Serializer for the User model.
    IsAuthenticated: Permission class that allows access only to authenticated users.
Classes:
    UserListView(generics.ListAPIView):
        A view that provides a read-only endpoint to list all users.
        Attributes:
            queryset: A queryset of all User objects.
            serializer_class: The serializer class used to serialize User objects.
            permission_classes: A list of permission classes that restrict access to authenticated users only.
"""
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]



