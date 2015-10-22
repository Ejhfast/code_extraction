# Send an email once object meets certain criteria
if not (Follower.objects.filter(company=company).count() % 5):
        #send the email
