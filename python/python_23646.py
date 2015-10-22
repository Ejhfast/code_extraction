# Adding variable to a foreignkey form
location = Location.objects.get(pk=location_id)
form.location = location
