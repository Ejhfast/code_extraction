# PyGObject (Glade) Window Never Showing (Multithreaded)
if Gtk.events_pending():
    Gtk.main_iteration()
