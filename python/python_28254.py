# Creating a test suite from multiple test cases
suite1 = unittest.TestLoader().loadTestsFromTestCase(TestOne)
suite2 = unittest.TestLoader().loadTestsFromTestCase(TestTwo)
alltests = unittest.TestSuite([suite1, suite2])
