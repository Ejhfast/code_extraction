# How to change colors of multiple widgets after hovering in Tkinter?
Hover1.bind("&lt;Enter&gt;", lambda event, h=Hover1: h.configure(bg="red"))
