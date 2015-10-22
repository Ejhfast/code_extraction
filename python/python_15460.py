# Can't import module from bin directory of the same project
import sys,os
sys.path.append(os.path.abspath('..'))
from myproj.logger import LOG
