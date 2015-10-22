# (Django) (Foreign Key Issues) model.person_id May not be NULL
personal = form.save(commit = False)
personal.person = request.user
personal.save()
