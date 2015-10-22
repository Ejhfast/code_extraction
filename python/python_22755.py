# How can i create my own SIGNAL and channel it to a SLOT?
self.UsrName = QLineEdit("username")
self.UsrName.mousePressEvent = lambda event: self.UsrName.clear()
