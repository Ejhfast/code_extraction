# Order by reverse ForeignKey DateTimeField?
threads = pm_thread.objects.filter(participants=request.user).order_by('-pm_message__datetime')
