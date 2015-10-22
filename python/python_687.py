# How to handle back and forward buttons in the hildon.Seekbar?
seekbar.connect("value-changed", control_changed, label)
seekbar.connect("notify::fraction", fraction_changed, label)
