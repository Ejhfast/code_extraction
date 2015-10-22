# Django: initial validating a form created from object instance, not POST
if request.session.get('trying_to_publish', False):
    form = FinalForm({}, instance=project)
    form.is_valid()
