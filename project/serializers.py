from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'title', 'description', 'techonology', 'createdAdd')
        read_only_fields = ('createdAdd',) # Campos de solo lectura, no se modificará la fecha de creación
# Compare this snippet from project/views.py: