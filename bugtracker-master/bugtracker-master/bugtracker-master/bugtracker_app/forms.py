# bugtracker_app/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, TicketModel

class SignupForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ["displayname"]
    username = forms.CharField(max_length=130)
    password = forms.CharField(widget=forms.PasswordInput)

class LoginForm(forms.Form):
    username = forms.CharField(max_length=130, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

class TicketForm(forms.Form):
    title = forms.CharField(max_length=65, required=True)
    description = forms.CharField(widget=forms.Textarea, required=True)
    priority = forms.ChoiceField(
        choices=TicketModel.PRIORITY_CHOICES,
        initial='media',  # Establece el valor por defecto que desees
    )

class EditTicketForm(forms.ModelForm):
    class Meta:
        model = TicketModel
        fields = [
            'description',
            'title',
            'priority',
        ]
