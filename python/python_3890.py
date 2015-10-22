# What resources are there for A/B split-testing in Python?
from swab import Swab
s = Swab('/tmp/.swab-test-data')
s.addexperiment('button-size', ['default', 'larger'], 'order-completed')
