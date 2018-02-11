__author__ = 'Dunga'
from django import forms
from .models import Todo


class TodoForm(forms.ModelForm):
    title = forms.CharField(max_length=50)
    text = forms.Textarea()


    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Todo
        fields = ['title', 'text']
