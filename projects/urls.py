from django.urls import path, include
from . import views

urlpatterns = [
    path('user-projects', views.UserProjectView.as_view(), name='user-projects'),
    path('create', views.create_project, name="create-project"),
    path('update/<uuid:pk>', views.update_project, name='update-project'),
    path('<uuid:pk>', views.project_details, name="project-details")
]