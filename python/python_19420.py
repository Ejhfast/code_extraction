# Sending email from a Django app hosted on Heroku with attachment stored in AWS S3
message = EmailMessage(subject, body, from_email, bcc=recipient_list)
message.attach(FILENAME, mymodel.myfilefield.read())
