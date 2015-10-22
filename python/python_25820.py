# call different functions based on parameter
def verify(self, param, val):
    self.assertEqual(getattr(self.tm.get, param), val)
