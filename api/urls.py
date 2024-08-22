from django.urls import path
from .views import get_project, create_project, project_detail

urlpatterns = [
    path('project/', get_project, name='get_project'),
    path('project/create/', create_project, name='create_project'),
    path('project/<int:pk>/', project_detail, name='project_detail')
]