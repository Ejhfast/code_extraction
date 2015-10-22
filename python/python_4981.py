# How can I send an email using python in google app engine
message = mail.EmailMessage(sender="&lt;emailid&gt;",subject="Output",to="&lt;emailid&gt;"))
message.body = ""
message.send()
