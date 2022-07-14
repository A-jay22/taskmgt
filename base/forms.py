from django.forms import ModelForm
from . models import Task, Activities


class ActivityForm(ModelForm):    
    class Meta:
        model = Activities
        fields = '__all__'

class TaskForm(ModelForm):
    class Meta:
        model = Task 
        fields = '__all__'

# class Tform(forms.Form):
#     task = forms.charfield(label='task', max_length=200)
#     descrition = forms.charfield(label='description', max_length=200)
#     complete = forms.ckeckbox(default=Off)
    


