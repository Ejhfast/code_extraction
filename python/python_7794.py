# GtkSpinButton disabled by default in Glade
adj = gtk.Adjustment(1, 1, 99, 1, 1, 1)
spinBtn = self.builder.get_object("spinbutton1")
spinBtn.configure(adj, 1, 0)
