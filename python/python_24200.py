# Setting a Generic Foreign Key in Django while still sane
stream_instance = stream_form.save(commit=False)
stream_instance.content_object = attempt
stream_instance.save()
