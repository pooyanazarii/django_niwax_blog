from django.contrib import admin
from iblog.models import Post


# Register your models here.

#this class for customize show data in admin

@admin.register(Post)
class PostAdmin_customize (admin.ModelAdmin):
    date_hierarchy = 'created_date'
    #this is show when you see list of post
    list_display = ('id','title','status','counted_view','author','published_date')
    #this is show when you edit
    fields =('title','text_content','author','category','counted_view','status','published_date','created_date','updated_date')
    #for search in admin
    search_fields = ['title','text_content','author']
    
# admin.site.register(Post,PostAdmin_customize)