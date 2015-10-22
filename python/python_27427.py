# How to add a "Body" to a python mime multipart(has attachment) email
body = "Text for body"
msg.attach(MIMEText(body,'plain'))
