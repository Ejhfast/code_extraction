# python win32api blocking bottle routes
from gevent import monkey
monkey.patch_all(thread=False)
