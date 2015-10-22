# Print into console terminal not into cell output of IPython Notebook
import sys
sys.stdout = open('/dev/stdout', 'w')
