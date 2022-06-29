from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    title = models.CharField(max_length=45, null=False)
    description = models.TextField(null=False)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        ordering = ['created']


    def __str__(self):
        return self.title   

class Activities(models.Model):
    title = models.CharField(max_length=45, null=False)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)  
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['updated', 'created']


    def __str__(self):
        return self.title