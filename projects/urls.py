from django.urls import path, include
from . import views

urlpatterns = [
    path('user-projects', views.UserProjectView.as_view(), name='user-projects'),
    path('create-project', views.create_project, name="create-project")
]