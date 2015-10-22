# Convert SQL query to Django friendly format for application
users_to_exclude = Noticesetting.objects.filter(send=False, notice_type__label='announcement').values('user')
emails = Emailaddress.objects.exclude(user__in=users_to_exclude)
