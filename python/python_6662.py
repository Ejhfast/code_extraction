# How to display rich text in a gtk.MenuItem label?
label = menuItem.get_children()[0]
        label.set_markup("&lt;b&gt;Hi Pete!&lt;/b&gt;")
