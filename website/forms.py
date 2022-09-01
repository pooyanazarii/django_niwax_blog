from email.policy import default
from django import forms
from website.models import Contact
from django.utils import timezone

class ContactForm(forms.ModelForm):
    
    class Meta:
        model = Contact
        fields = ['subject','email','number','message']
        # fields = ['name','subject','email','number','message']
        required_fields = ['subject','email','number','message']

        