# Is storing pyQT widgets in a list bad form?
for i in reversed(range(layout.count())):
    layout.itemAt(i).widget().setParent(None)
