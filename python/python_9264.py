# Django using url to get only the url part of a named view with parameters
url(r'^test/(\d+)/$', 'test_view', name='test-view'),
url(r'^test/$', 'test_view', name='test-view'),
