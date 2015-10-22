# How to remove property of ui component in pyside/pyqt?
self.ui.txtName.setProperty("rules", QtCore.QVariant())
#or
self.ui.txtName.setProperty("rules", None)
