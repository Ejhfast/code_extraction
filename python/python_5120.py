# How to create a gsignal without parameters in pygtk
__gsignals__ = {
  "some-signal": (gobject.SIGNAL_RUN_FIRST, gobject.TYPE_NONE, ()),
}
