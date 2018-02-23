__author__ = 'Dunga'
from django.contrib.auth.models import User
from django import forms
from .models import Todo


class TodoForm(forms.Form):
    title = forms.CharField(max_length=50)
    text = forms.Textarea()


    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Todo
        fields = ['title', 'text']


class UserCreationForm(forms.ModelForm):
    username = forms.CharField(label="Username", max_length=30, widget=forms.TextInput)
    email = forms.CharField(label="email", max_length=30, widget=forms.TextInput)
    password = forms.CharField(label="Password", max_length=30, widget=forms.PasswordInput)
    #password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']