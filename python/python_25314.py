# Need file dialog for code running in Enthought Canopy
from PySide import QtGui
fname, _ = QtGui.QFileDialog.getOpenFileName(None, 'Choose file','.')
