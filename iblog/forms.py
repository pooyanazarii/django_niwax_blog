from django import forms
from iblog.models import Comment


# class NameFrom(forms.Form):
#     name = forms.CharField(max_length=255)
#     email = forms.EmailField()
#     subject = forms.CharField(max_length=255)
#     message = forms.CharField(widget=forms.Textarea)

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        # fields = "__all__"
        fields = ['post','name','email','subject','message']
        