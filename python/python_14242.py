# GAE Python - How to attach the results of csv.writer to an email?
message = mail.EmailMessage(sender="Me &lt;me@gmail.com&gt;",
        subject="Shop Export",
        attachments=[("shops.csv", self.response.body)])
