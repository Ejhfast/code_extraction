# how to change the test description of python (2.7) untitest
from unittest.runner import TextTestResult
TextTestResult.getDescription = lambda _, test: test.shortDescription()
