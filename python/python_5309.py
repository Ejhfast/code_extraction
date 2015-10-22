# How to clear form fields after a submit in Django
if form.is_valid():
    form.save()
    return http.HttpResponseRedirect('')
