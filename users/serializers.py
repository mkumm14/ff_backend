# serializers.py
"""
serializers.py
This module defines custom serializers for user authentication and registration using Django REST framework and dj-rest-auth.
Classes:
    UserSerializer: A serializer for the Django User model, including fields for id, username, email, first name, and last name.
    CustomLoginSerializer: A custom login serializer that extends dj-rest-auth's LoginSerializer, with the email field set to None.
    CustomRegisterSerializer: A custom registration serializer that extends dj-rest-auth's RegisterSerializer, adding first name and last name fields. Overrides the get_cleaned_data method to include these fields in the cleaned data.

"""
from django.contrib.auth.models import User
from dj_rest_auth.serializers import LoginSerializer
from dj_rest_auth.registration.serializers import RegisterSerializer

from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']


class CustomLoginSerializer(LoginSerializer):
    email=None


class CustomRegisterSerializer(RegisterSerializer):
    first_name = serializers.CharField(write_only=True,allow_blank=True)
    last_name = serializers.CharField(write_only=True,allow_blank=True)
    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
            'first_name':self.validated_data.get('first_name', ''),
            'last_name':self.validated_data.get('last_name', ''),

        }
    


