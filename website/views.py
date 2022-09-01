from django.shortcuts import render
from website.forms import ContactForm
from website.models import Contact

# Create your views here.
def contactus_view(request):
    forms = ContactForm()
    if request.method == 'POST':
        forms = ContactForm(request.POST)
        # name = request.POST.get('name')
        # email = request.POST.get('email')
        # subject = request.POST.get('subject')
        # number = request.POST.get('number')
        # message = request.POST.get('message')
        # print(name,email,subject,number,message)
        # contact = Contact()
        # contact.name = name
        # contact.email = email
        # contact.subject = subject
        # contact.number = number
        # contact.message = message
        if forms.is_valid():
            name = forms.cleaned_data['name']
            email = forms.cleaned_data['email']
            subject = forms.cleaned_data['subject']
            number = forms.cleaned_data['number']
            message = forms.cleaned_data['message']
            forms.save()
        print("-----------------------------")
    forms= {"forms":forms}
    return render(request,'website_pages/contact-us.html',forms)
