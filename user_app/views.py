#-*- coding: utf-8 -*-
#import the built-in generic view to add or update a user
from django.views.generic import CreateView, DetailView, UpdateView
from django.contrib import messages
from user_app.forms import AddProfileForm, UpdateProfileForm
from user_app.models import UserModel


#Q0: add a user's profile (registration)
class AddProfile(CreateView):
	form_class = AddProfileForm
	template_name = "user_app/add_profile.html"
	success_url="/user_app/add_profile"


	#add a success message if the form is valid
	def form_valid(self, form):
		messages.success(self.request, "The user's profile has been saved.", extra_tags='success')
		return super(AddProfile, self).form_valid(form)



#Q1: display user's profile
class ShowProfile(DetailView):
	model=UserModel
	template_name = "user_app/show_profile.html"

	#display the current user's profile
	def get_object(self):
		return UserModel.objects.get(pk=self.request.GET.get('pk'))



#~ # Q5: view to update a user
class UpdateProfile(UpdateView):

	#call the form to modify a user
	form_class = UpdateProfileForm
	#use the template of modification of a new user
	template_name = "user_app/update_profile.html"

	#once the profile updated, redirect to a "success_url" (same url -> we stay on the update profile page)
	def get_success_url(self):
		succ_url =  '/user_app/update_profile?pk='+self.request.GET.get('pk')
		return succ_url

	#add a success message if the form is valid
	def form_valid(self, form):
		messages.success(self.request, "Your profile has been updated.", extra_tags='success')
		return super(UpdateProfile, self).form_valid(form)
#~ #~
	#modifcation: display the user's data given his primary key
	def get_object(self):
		return UserModel.objects.get(pk=self.request.GET.get('pk'))
