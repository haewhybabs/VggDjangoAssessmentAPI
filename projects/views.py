from django.shortcuts import render
from rest_framework import viewsets
from .models import Project
from .models import Action
from .serializers import ProjectSerializer
from .serializers import ActionSerializer
from rest_framework import generics

class ProjectView(viewsets.ModelViewSet):
    queryset= Project.objects.all()
    serializer_class=ProjectSerializer
class ActionView(viewsets.ModelViewSet):
    queryset= Action.objects.all()
    serializer_class=ActionSerializer
    
    
class ProjectActions(generics.ListAPIView):
    serializer_class=ActionSerializer
    def get_queryset(self):
        id=self.kwargs['id']
        return Action.objects.filter(project_id__exact=id)
    

