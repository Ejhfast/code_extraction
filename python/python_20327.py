# Import Error embedding IPython into PyQt application
import sip
sip.setapi('QString', 2)
from PyQt4 import QtGui
