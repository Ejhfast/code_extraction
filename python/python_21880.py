# Validate webapp2 request arguments are present
for each in ['handle', 'phone_number']:
    if each not in self.request.POST:
        # your error code here
