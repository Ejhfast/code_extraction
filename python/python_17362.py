# Python 2.7.2 shelve fails on OSX
import anydbm
anydbm._defaultmod = __import__('dumbdbm')
