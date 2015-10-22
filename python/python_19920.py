# Send email to multiple addresses (using cc) from different domains
server.sendmail("me@mydomain.com", toEmails+ccEmails, msg.as_string())
