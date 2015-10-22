# reading pyqt stylesheet from external qss file
sshFile="darkorange.stylesheet"
with open(sshFile,"r") as fh:
    self.setStyleSheet(fh.read())
