# How do I "print" something to the console in pylons?
import logging
log = logging.getLogger(__name__)
log.debug('hello world')
