from django.conf.urls import url
from . import views

urlpatterns = [
               url(r'newuser', views.newuser, name='newuser'),
			   url(r'^$', views.home, name='home'),
              ]