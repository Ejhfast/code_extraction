# Setting Tkinter default widgets kwargs
def resetUI(self, bg=None, fg=None):
    for button in list_of_buttons:
        button.config(background=bg, foreground=fg)
