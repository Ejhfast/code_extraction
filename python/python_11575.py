# PyGTK/Gobject waiting for pending tasks
##  force the refresh of the screen
            while gtk.events_pending():
                gtk.main_iteration()
