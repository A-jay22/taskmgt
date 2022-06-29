from django.forms import ModelForm
from . models import Activities

class ActivityForm(ModelForm):
    class Meta:
        model = Activities
        fields = '__all__'

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'


