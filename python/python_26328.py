# Growing a widget vertically when resizing the window (using the grid geometry manager)
root.rowconfigure(1, weight=1)
# [...]
text.grid(row=1, column=0, sticky=tk.W + tk.E + tk.N + tk.S)
