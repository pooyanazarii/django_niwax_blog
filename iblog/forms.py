from django import forms
from iblog.models import Contact
from django.forms import ModelForm

class NameFrom(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    subject = forms.CharField(max_length=255)
    message = forms.CharField(widget=forms.Textarea)

class ContactForm(forms.ModelForm):
    
    class Meta:
        model = Contact
        # fields = "__all__"
        exclude = ["created_date","updated_date"]
        