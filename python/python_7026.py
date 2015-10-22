# Logging problems when using modules individually
import logging
logging.getLogger('your_top_level_package').addHandler(logging.NullHandler())
