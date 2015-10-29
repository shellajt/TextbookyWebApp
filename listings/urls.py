from django.conf.urls import url
from . import views

urlpatterns = [
               url(r'newlisting', views.newlisting, name='newlisting'),
			   url(r'^$', views.listing_list, name='listing_list'),
              ]