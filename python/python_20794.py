# PyQt: How to set Combobox to Item knowing Item's text (a title)
index = combo.findText(text, QtCore.Qt.MatchFixedString)
    if index &gt;= 0:
         combo.setCurrentIndex(index)
