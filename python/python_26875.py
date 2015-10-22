# What is the meaning of the a(ss) type in the dconf, and what are the correct methods of gi.repository.Gio.Settings to get/set such fields?
from gi.overrides import GLib
value1 = entries.get_value(key1).unpack() # returns e.g. [("a", "b"), ("c", "d")]
entries.set_value(key2, GLib.Variant("a(ss)", value2)) # value2 is e.g. [("a", "b"), ("c", "d")]
