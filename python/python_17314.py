# how to change Qtablewidget's spesific cells backround color in pyqt
self.tableWidget.setItem(3, 5, QtGui.QTableWidgetItem())
self.tableWidget.item(3, 5).setBackground(QtGui.QColor(100,100,150))
