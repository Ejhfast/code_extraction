# Only allow 1 instance of a python script
import os
os.open("lock", os.O_CREAT|os.O_EXCL)
