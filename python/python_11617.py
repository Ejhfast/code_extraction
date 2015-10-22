# lift a tkMessageBox
tl2 = tk.Toplevel(...)
...
tkMessageBox.showinfo("Say Hello", "Hello World", parent=tl2)
