from .models import Task
from django.forms import ModelForm 

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        exclude = ['complete', 'user']

class TaskUpdate(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        exclude = ['user']