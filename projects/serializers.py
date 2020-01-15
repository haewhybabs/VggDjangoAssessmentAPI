from rest_framework import serializers
from .models import Project
from.models import Action

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=Project
        fields=('id','name','description','completed')

class ActionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Action
        fields=('id','project_id','description','notes','completed')