# My cookies are not being transmitted when using webtest.TestApp
self.testapp.post_json('/comment',
                       {'value': ""},
                       extra_environ={'wsgi.url_scheme': 'https'})
