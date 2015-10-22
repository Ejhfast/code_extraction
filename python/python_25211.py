# How to make my test fixtures loaded only while testing in Django?
class AnimalTestCase(TestCase):
      fixtures = ['mammals.json', 'birds']
