# How to set the default item of a QComboBox
self.appExeCB=QtGui.QComboBox()
self.appExeCB.addItems(self.items.keys())
self.appExeCB.setCurrentIndex(self.items.keys().index('Maya Executable'))
