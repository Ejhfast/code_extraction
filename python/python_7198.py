# how to get all folder only in a given path in python?
import os.path
dirs = [d for d in os.listdir('Tools') if os.path.isdir(os.path.join('Tools', d))]
