# What's the proper way to test token-based auth using APIRequestFactory?
request = self.factory.get('/my_endpoint', HTTP_AUTHORIZATION='Token {}'.format(self.token))
force_authenticate(request, user=self.user)
