# Django Testing: Using a login decorator for test cases
class SimpleTest(TestCase):
    def setUp(self):
        self.client.login(username='foo', password='bar')
