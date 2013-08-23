from django.db import models
from django.contrib.auth.models import User, UserManager
from django.dispatch import receiver
from django.db.models.signals import pre_save

# Q1 : user's profile -> extends the built-in User class containing username, email,  password, first_name, last_name
class UserModel(User):
	"""Built-in User class with app settings."""
	date_of_birth = models.DateField(max_length=10)
	biography = models.TextField(max_length=1000)
	contacts = models.CharField(max_length=100)

	# Use UserManager to get the create_user method, etc.
	objects = UserManager()

	#for convenience, the username is the unique id of the user
	#it would be better to use the email instead (e.g.: for the authentication), but django uses the username and it would be lots of work to do to replace the username with the email
	#checks the uniqueness of the email field
	#~ @receiver(pre_save, sender=User)
	#~ def User_pre_save(sender, **kwargs):
		#~ email = kwargs['instance'].email
		#~ username = kwargs['instance'].username
		#~ if not email: raise ValidationError("email required")
		#~ if sender.objects.filter(email=email).exclude(username=username).count(): raise ValidationError("email needs to be unique")
