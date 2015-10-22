# PySide + QtSql - cannot load database drivers
site_pack_path = site.getsitepackages()[1]
QtGui.QApplication.addLibraryPath('{0}\\PySide\\plugins'.format(site_pack_path))
