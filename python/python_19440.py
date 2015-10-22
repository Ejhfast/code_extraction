# How do I call one Flask view from another one?
client = app.test_client()
response = client.get('/your/url', headers=list(request.headers))
