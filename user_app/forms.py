from django.forms import ModelForm
from models import UserModel
from django import forms
from django.conf import settings


# Q0 : create a form to add a user
class AddProfileForm(ModelForm):
	password = forms.CharField(max_length=30,widget=forms.PasswordInput())
	password_verify = forms.CharField(max_length=30,widget=forms.PasswordInput(), label='Retype password')
	#Q6: display a calendar instead of a textbox for the date of birth
	date_of_birth =forms.DateField(widget=forms.TextInput(attrs={'class' : 'datepicker'}))

	class Meta:
		model = UserModel
		fields=("username", "password", "password_verify", "first_name", "last_name", "date_of_birth", "biography", "contacts", )

	#called on validation of the form
	# do passwords submitted match each other?
	def clean(self):
		if 'password' in self.cleaned_data and 'password_verify' in self.cleaned_data:   # check if both passwords entered
			if self.cleaned_data['password'] != self.cleaned_data['password_verify']:    # check if they match each other
				raise forms.ValidationError("Passwords do not match!")
			else:
				return self.cleaned_data

	#hash the password before saving
	def save(self, commit=True):
		user = super(AddProfileForm, self).save(commit=False)
		user.set_password(self.cleaned_data["password"])
		if commit:
			user.save()
		return user


# Q5 : create a form to modify a user's profile
class UpdateProfileForm(ModelForm):
	#call the model to create the form
	#Q6: display a calendar instead of a textbox for the date of birth
	date_of_birth =forms.DateField(widget=forms.TextInput(attrs={'class' : 'datepicker'}))
	class Meta:
		model = UserModel
		fields=("first_name", "last_name", "date_of_birth", "biography", "contacts", )

	#Q7: reverse the order of the fields
	def __init__(self, *args, **kwargs):
		super(UpdateProfileForm, self).__init__(*args, **kwargs)
		self.fields.keyOrder = ["contacts", "biography", "date_of_birth",  "last_name",  "first_name"]
