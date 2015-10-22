# Check If a user belong to a group In views
request.user.groups.filter(name__in=['onetime','monthtime']).exists()
