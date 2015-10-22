# Save user input into a Text widget Tkinter when using classes
self.bottom = ScrolledText(m2, wrap=WORD)
...
print self.bottom.get("1.0", "end-1c")
