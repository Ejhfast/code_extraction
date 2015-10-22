# Python Outlook getting all emails from Sender
for m in messages:
   if m.SenderEmailAddress == 'some_sender@somewhere.com':
       print(m)
