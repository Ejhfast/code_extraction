# Validate stored data against a form in django
form = PersonForm({'firstname':person.firstname,.....})
is_valid = form.is_valid()
