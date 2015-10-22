# How to import package modules from in-package "main" module
import os
os.sys.path.append(os.path.dirname(os.path.realpath(__file__))+ '/../../')
