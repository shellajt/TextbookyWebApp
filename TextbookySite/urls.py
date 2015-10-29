from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    # Examples:
    # url(r'^home/', 'Textbooky.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'home.views.home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^listings/', include('listings.urls')),
	url(r'^home/', include('home.urls')),
]
