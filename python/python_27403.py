# Python requests returns: CSRF verification failed. Request aborted
resp = session.get('http://mywebsite.com')
csrftoken = resp.cookies['ThisIsMyToken']
