# Tk/Tkinter: Detect application lost focus
def app_lost_focus(self, event):
    if self.focus_get() != self.menu:
        self.destroy_menu(event)
