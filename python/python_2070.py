# django send_mail from queryset
UserProfile.objects.filter(mailCom='1').values_list('email', flat=True)
