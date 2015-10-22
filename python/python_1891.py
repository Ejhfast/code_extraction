# using os.path is quite verbose is there a more concise way to manipulate paths
from os.path import dirname,realpath
sys.path.append(dirname(dirname(realpath(__file__))))
