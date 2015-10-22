# Dynamically create tabs QTabWidget and fill tables QTableWidget
page = self.ui.tabWidget.widget(index)
    tablewidget = page.findChild(QTableWidget)
