from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['subject', 'notes']  # Include all fields you want to edit/add
