from django.conf.urls.defaults import patterns, include, url
from image import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
)
