#went through this in auth demo refer to Login and SignupForm there
# bugtracker_app/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, TicketModel

class SignupForm(forms.ModelForm): #SignupForm
    class Meta:
        model = CustomUser
        fields = ["displayname"]
    username = forms.CharField(max_length=130)
    password = forms.CharField(widget=forms.PasswordInput)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

class TicketForm(forms.Form):
    title = forms.CharField(max_length=65, required=True)
    description = forms.CharField(widget=forms.Textarea, required=True)
    priority = forms.ChoiceField(choices=[('alta', 'Alta'), ('media', 'Media'), ('baja', 'Baja')])
class EditTicketForm(forms.ModelForm):
    class Meta:
        model = TicketModel
        fields = [
            #'status'
            #'assignedto'
            'description',
            'title'
        ]
