# google app engine datastore unique id
message_key = Message(name = self.request.get('name'), email : self.request.get('email')).put()
