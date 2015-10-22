# Django from JSON format
klass = type('Form', (forms.Form,), fields)
form = klass()
return form
