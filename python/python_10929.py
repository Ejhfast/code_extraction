# How can I test multi-part uploads with FlaskClient (for unit testing)
builder = EnvironBuilder(method='POST', data={'foo': 'this is some text',
...      'file': (StringIO('my file contents'), 'test.txt')})
