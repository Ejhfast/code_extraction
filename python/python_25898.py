# How do you change the display name when sending emails via Amazon SES in Django?
email_message = EmailMessage('This is a title', 'This is a message body', 'UserFirstName UserLastName &lt;FromEmail@example.com&gt;', ['ToEmail@example.com'])
