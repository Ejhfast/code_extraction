# Django complex Query through database API
profile = EnterpriseProfile.objects.get(pk=1)  # or whatever to get the object
# next returns all users related to that enterprise in the M2M
profile.enterprise.users.all()
