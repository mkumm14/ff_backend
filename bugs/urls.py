from django.urls import path, include
from . import views

urlpatterns = [
    path("<uuid:pk>/project-bugs", views.project_bugs, name="project-bugs")
]