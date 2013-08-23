from django.core.management.base import NoArgsCommand
from django.db import models
from django.db.models import Count

#Q9: command to display all the models objects and count them
#call the command from a terminal: python manage.py show_db
class Command(NoArgsCommand):
    help = 'Display all the model objects and cout their number'
    def handle(self, **options):
		models_list=models.get_models()
		#we loop over all the models
		for model in models_list:
			#model name
			self.stdout.write('MODEL: "%s"' % model._meta.db_table)
			#number of objects
			nb=model.objects.count()
			self.stdout.write('Number of records: "%s"' % nb)
			self.stdout.write('')
			#list of objects
			objects=model.objects.all()
			#list of fields
			columns=model._meta.get_all_field_names()
			#loop over the objects
			for obj in objects:
				#loop over the fields
				for column in columns:
					try:
						self.stdout.write(column+': '+str(getattr(obj, column)))
					except Exception, e:
						pass
						#~ print e
				self.stdout.write('')

			self.stdout.write('')
			self.stdout.write('----------------------------------------------------------')
			self.stdout.write('')
