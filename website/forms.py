from django import forms
from website.models import Contact

from captcha.fields import CaptchaField

class ContactForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Contact
        fields = ['subject','email','number','message']
        # fields = ['name','subject','email','number','message']
        required_fields = ['subject','email','number','message']


        