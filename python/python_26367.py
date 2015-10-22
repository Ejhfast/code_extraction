# How to send requests with JSONs in unit tests
response=self.app.post('/test_function',
                       data=json.dumps(dict(foo='bar')),
                       content_type = 'application/json')
