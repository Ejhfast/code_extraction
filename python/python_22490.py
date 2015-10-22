# need display to be on 3 lines not 1 line
def show_info(self):
    lines = ['My Name', '123 Any Rd', 'Town Fl, 12345']
    tkinter.messagebox.showinfo('Text', "\n".join(lines))
