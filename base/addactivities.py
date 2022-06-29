from django.forms import ModelForm
from . models import Activities

class AddActivities(ModelForm):
    class Meta:
        model = Activities
        fields = '__all__'

