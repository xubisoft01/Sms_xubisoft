
from django.forms import ModelForm, ValidationError
from .models import  Contact_U
from django.forms import forms



class ContactForm(ModelForm):
    class Meta:
        model = Contact_U
        fields = ['name', 'email', 'messages']

