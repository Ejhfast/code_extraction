# act on all children at once on pyqt widget
[textEditor.clear() for textEditor in myGroupBox.findChildren(QtGui.QTextEdit)]
