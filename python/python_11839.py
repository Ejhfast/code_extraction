# Grab the focus from GTK popup menu
gdk_pointer_ungrab(GDK_CURRENT_TIME);
gdk_keyboard_ungrab(GDK_CURRENT_TIME);
gtk_grab_remove(menu);
