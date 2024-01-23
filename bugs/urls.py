from django.urls import path, include
from .views import BugsByProjectView

urlpatterns = [
    path("<uuid:pk>/project-bugs", BugsByProjectView.as_view(), name='project_bugs')
]