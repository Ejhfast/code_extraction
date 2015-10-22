# Python & GTK3: How to create a Liststore
from gi.repository import Gtk, GdkPixbuf
store = Gtk.ListStore(str, GdkPixbuf.Pixbuf, bool)
