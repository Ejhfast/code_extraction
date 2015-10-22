# How do I hide Soap Faults in python suds?
import logging
logging.getLogger('suds.client').setLevel(logging.CRITICAL)
