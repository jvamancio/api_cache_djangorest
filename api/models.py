from django.db import models

# Create your models here.

class Projects(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    description = models.TextField(max_length=100)
    
    def __self__(self):
        return self.name