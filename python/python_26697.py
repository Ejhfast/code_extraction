# cannot change(edit) the file uploaded in django
customer_edit = update_customer_prof(request.POST, request.FILES, instance=request.user.customer_profile)
