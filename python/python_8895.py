# Received 403 CSRF verification failed when logging through python requests
r = requests.post(self.loginurl, data={'csrf_token': django.middleware.csrf.get_token(), 'username':self.username, 'password': self.password}, auth=(self.username, self.password),allow_redirects=True)
