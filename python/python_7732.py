# How do I change the data displayed, not the data itself, with QSqlTableModel?
self.model = QSqlTableModel(self)
self.model.setEditStrategy(QSqlTableModel.OnManualSubmit)
