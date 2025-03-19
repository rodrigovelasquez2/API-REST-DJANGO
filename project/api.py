from .models import Project
from rest_framework import viewsets, permissions
from .serializers import ProjectSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all() # Consulta todos los datos de una tabla
    permission_classes = [permissions.AllowAny] # Permisos de acceso
    serializer_class = ProjectSerializer # Clase serializadora

# Compare this snippet from project/urls.py:    