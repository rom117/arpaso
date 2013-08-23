from django.conf.urls import patterns, url
from user_app.views import AddProfile, ShowProfile, UpdateProfile
#Q2: redirect to login page if not logged
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
	#Q0: add a user
    (r'^add_profile', AddProfile.as_view()),
	#Q1: show user profile
	#Q2: cant access this page if not logged
    (r'^show_profile', login_required(ShowProfile.as_view())),
    #Q5: update profile
    (r'^update_profile', login_required(UpdateProfile.as_view())),
)
