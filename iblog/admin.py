from django.contrib import admin
from iblog.models import Post
from iblog.models import Tags
from iblog.models import Comment


from django_summernote.admin import SummernoteModelAdmin



# Register your models here.

#this class for customize show data in admin

admin.site.register(Tags)
@admin.register(Post)
class PostAdmin_customize (SummernoteModelAdmin):
    date_hierarchy = 'created_date'
    #this is show when you see list of post
    list_display = ('id','title','status','login_require','counted_view','author','published_date')
    #this is show when you edit
    fields =('login_require','image','title','text_content','tags','author','category','counted_view','status','published_date','created_date','updated_date')
    #for search in admin
    search_fields = ['title','text_content','author']
    summernote_fields = ('text_content',)
    
# admin.site.register(Post,PostAdmin_customize)
class CommentAdmin (admin.ModelAdmin):
    date_hierarchy = 'created_date'
    #this is show when you see list of post
    list_display = ('subject','id','approved', 'email','created_date','name')
    #this is show when you edit
    # fields =('image','title','text_content','tags','author','category','counted_view','status','published_date','created_date','updated_date')
    #for search in admin
    list_filter= ['approved','post']
    search_fields = ['subject','email','message']
admin.site.register(Comment,CommentAdmin)
