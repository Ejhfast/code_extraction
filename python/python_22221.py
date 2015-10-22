# Addiong Scrollbar to Tkinter Entry or Text widgets
txt.configure(state="disabled")
txt.bind("&lt;1&gt;", lambda event: txt.focus_set())
