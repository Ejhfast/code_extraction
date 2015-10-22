# Correct use of the .clear() method on QDateTimeEdit
def clearDate(self):
    self.MyInput.findChild(QtGui.QLineEdit).setText('')
