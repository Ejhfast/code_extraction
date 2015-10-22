# How to get list of subdirectories names
import os
output = [dI for dI in os.listdir('foo') if os.path.isdir(os.path.join('foo',dI))]
