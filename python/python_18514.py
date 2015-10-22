# simple IPython example raises exception on sys.exit()
app = QApplication(sys.argv)
app.aboutToQuit.connect(app.deleteLater)
