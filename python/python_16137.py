# Add HTTP_USER_AGENT to Django RequestFactory request?
request = self.factory.get(reverse('home'), HTTP_USER_AGENT='Mozilla/5.0')
