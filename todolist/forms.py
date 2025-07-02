from django import forms
from .models import TodoList
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Todolist_form(forms.ModelForm):
    class Meta:
        model = TodoList
        fields = ['title','desc','completed']
        #widgets is used to add custom classes to the fields in the form. Useful for css
        widgets = {
            'title': forms.TextInput(attrs={'class':"form-control"}),
            'desc': forms.Textarea(attrs={'class':"form-control"})
        }
class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email','password1','password2')

        widgets={
            'username' : forms.TextInput(attrs={'class':"form-control"}),
            'email' : forms.EmailInput(attrs={'class':"form-control"}),
            'password1' : forms.PasswordInput(attrs={'class':"form-control"}),
            'password2' : forms.PasswordInput(attrs={'class':"form-control"}),
        }