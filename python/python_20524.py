# Tkinter and thread. out of stack space (infinite loop?)
def do_every_second():
    cont.insert("end", str(n) + "\n")
    root.after(1000, do_every_second)
