from django.contrib import admin
from website.models import Contact
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ['name','subject','email','number','create_date','updated_date','id']


admin.site.register(Contact,ContactAdmin)
