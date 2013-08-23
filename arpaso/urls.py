from django.conf.urls import patterns, include, url
from arpaso.views import homepage
from django.conf import settings
from django.conf.urls.defaults import *
from django.conf.urls.static import static


urlpatterns = patterns('',
	#homepage
	url(r'^/?$', homepage),
	#Q2: authentication
	url(r'^auth/?$', 'auth.views.auth'),
	#Q0, Q1, Q5: user application (add, show and update profile)
	url(r'^user_app/?', include('user_app.urls')),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

