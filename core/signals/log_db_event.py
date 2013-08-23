from core.models import LogDBEvents


#Q10: saves a signal into the database
def log_handler (signal_type, sender, **kwargs):
	#do not save events from LogDBEvents (otherwise unfinite calls!)
	if sender != LogDBEvents:
		LogDBEvents(event_type=signal_type,
				info="%s model changed with new entry %s"%(
						sender.__name__,
						kwargs['instance'])
		).save()

#Q10: a create or add signal is intercepted
def save_handler(sender, **kwargs):
	if kwargs['created']:
		return log_handler ('DC', sender, **kwargs)
	else:
		return log_handler ('DE', sender, **kwargs)

#Q10: a delete signal is intercepted
def del_handler(sender, **kwargs):
	return log_handler ('DD', sender, **kwargs)



