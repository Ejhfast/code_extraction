# Facebook app on app engine showing as blank page on canvas iframe
if u'signed_request' in self.request.POST:
    facebook.load_signed_request(self.request.get('signed_request'))
