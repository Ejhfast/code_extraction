# How to write a unittest with setUpClass & tearDownClass in Python 2.3
class MyTest(unittest.TestCase):
    def setUpClass(cls): ...
    setUpClass = classmethod(setUpClass)
