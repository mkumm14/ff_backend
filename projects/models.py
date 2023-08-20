from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Project(models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField()
    owner=models.ForeignKey(User, on_delete=models.CASCADE)
    users=models.ManyToManyField(User, related_name='assigned_projects')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='updated_projects', null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title
    
