# Django schedule a "one time" task based on datetime model attribute
task.apply_async([ev_objects], eta=my_eta, task_id=my_task_id)
