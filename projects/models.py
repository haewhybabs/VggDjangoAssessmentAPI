from django.db import models

# Create your models here.
class Project(models.Model):
    name=models.CharField(max_length=50)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
class Action(models.Model):
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    description=models.CharField(max_length=128)
    notes=models.TextField()
    completed=models.BooleanField(default=False)
    