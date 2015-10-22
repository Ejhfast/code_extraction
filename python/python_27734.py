# Django LiveServerTestCase: disable SSL at test-time
getattr(settings, 'UNDER_TEST', False)
