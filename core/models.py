from django.db import models
from core.signals.log_db_event import save_handler, del_handler
from django.db.models.signals import post_save, post_delete

#Q10 create model to store database events
class LogDBEvents(models.Model):
	EVENTS= (
		('DC','Database entry created'),
		('DD','Database entry deleted'),
		('DE','Database entry edited'),
	)
	event_time = models.DateTimeField(auto_now_add=True)
	event_type = models.CharField(choices=EVENTS, max_length=2)
	info = models.TextField()


#start a listener for INSERT INTO or UPDATE queries
post_save.connect(save_handler, dispatch_uid='post_save')
#start a listener for DELETE queries
post_delete.connect(del_handler, dispatch_uid='post_delete')
