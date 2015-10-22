# Celery: access to time of last run of task?
def after_return(self, status, retval, task_id, args, kwargs, einfo):
    #exit point for context managers
    self.taskLogger.__exit__(status, retval, task_id, args, kwargs, einfo)
