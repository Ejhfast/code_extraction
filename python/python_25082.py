# Python - ToggleButton - Possible to cancel the callback during once time?
self.bouton.disconnect_by_func(self.fonct)
self.bouton.set_active(False)
self.bouton.connect("clicked", self.fonct)
