"""bniwax_pj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.urls import include

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.sitemaps.views import sitemap
from website.sitemaps import StaticViewSitemap
from iblog.sitemaps import BlogSitemap
from account.views import login_view,logout_view,signup_view
from .views import *
import debug_toolbar
#-------------------------------------
# # here you can set website 
updating_flag =1
#-------------------------------------
sitemaps = {
    'static': StaticViewSitemap,
    'blog': BlogSitemap
}

urlpatterns = [
    path('robots.txt', include('robots.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
    path('summernote/', include('django_summernote.urls')),
    path('captcha/', include('captcha.urls')),
    path('admin/', admin.site.urls),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('accounts/login/', login_view, name='login'),
    path('accounts/logout/', logout_view, name='logout'),
    path('accounts/signup/', signup_view, name='signup'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns +=[
    # path('',include('iblog.urls')),
    path('website/',include('website.urls')),
    path('accounts/',include('account.urls')),
]

if updating_flag:
    urlpatterns +=[
    path('',upgrating_view1),
    path('blog',include('iblog.urls'))

    ]
else:
    urlpatterns +=[
    path('',include('iblog.urls')),
    ]
    


handler404 = 'iblog.views.handler404'