# PySide: QWidget does not draw background color
ui = MainWindow()
ui.setupUi(mainwindow)
ui.widget.setAttribute(QtCore.Qt.WA_StyledBackground, True)
