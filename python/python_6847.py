# FileChooserDialog stuck on screen after destroy()
while gtk.events_pending(): #   this forces the refresh of the screen
            gtk.main_iteration()
