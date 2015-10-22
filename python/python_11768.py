# Error Displaying Readable Text In Django Template
msg=EmailMessage(Subject, message.render(Context()),
    from_email, Invite.objects.values_list('email_address', flat=True))
