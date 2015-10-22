# How can I fake request.POST and GET params for unit testing in Flask?
self.app.post('/path-to-request', data=dict(var1='data1', var2='data2', ...))
self.app.get('/path-to-request')
