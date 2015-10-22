# how to wait to force subroutine to show widget before it continue to next line
self.processing_label.show()
QtGui.qApp.processEvents() # or QtCore.QCoreApplication.processEvents()
self.qry_db()
