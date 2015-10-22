# How to realize wx.EVT_KILL_FOCUS and wx.lib.intctrl.IntCtrl in PySide?
QObject.connect(app, SIGNAL("focusChanged(QWidget *, QWidget *)"), changedFocusSlot)
