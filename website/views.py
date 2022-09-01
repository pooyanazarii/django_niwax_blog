from django.shortcuts import render
from website.forms import ContactForm
from django.http import HttpResponseRedirect
from django.contrib import messages

# Create your views here.
def contactus_view(request): 
    forms = ContactForm()
    if request.method == 'POST':
        forms = ContactForm(request.POST)
        if forms.is_valid():
            forms.save()
            #redirect an show message successfully
            # messages.success(request,"success")
            messages.add_message(request, messages.SUCCESS, 'با موفقیت انجام شد.')
            return HttpResponseRedirect('/website/contact/')
            
        else:
            #redirect an show message Unsuccessfully
            messages.add_message(request, messages.ERROR, 'عملیات با شکست مواجه شد.')
            return HttpResponseRedirect('/website/contact/')
    forms = {"forms": forms}
    
    return render(request, 'website_pages/contact-us.html', forms)
