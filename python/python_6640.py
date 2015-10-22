# Get location of the .py source file
# in /a/b/c/d/e/file.py
import os
os.path.dirname(os.path.abspath(__file__)) # /a/b/c/d/e
