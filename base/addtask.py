from django.forms import ModelForm
from . models import Task

class AddTask(ModelForm):
    class Meta:
        model = Task
        # fields = ['title', 'description', 'complete']
        fields ='__all__'

