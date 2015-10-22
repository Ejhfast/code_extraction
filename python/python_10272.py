# python setting application icon
root = Tk()
img = PhotoImage(file='your-icon')
root.tk.call('wm', 'iconphoto', root._w, img)
