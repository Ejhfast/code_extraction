# Trying to import class from a module in the same package by a string
from importlib import import_module
import_module(str("." + market), 'market')
