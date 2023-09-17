from django import forms
from .models import Task, Photo

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['image']