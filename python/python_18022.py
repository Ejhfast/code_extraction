# how to get whole line text, on which I got cursor
view = self.window.active_view()
line = view.line(view.sel()[0])
linetext = view.substr(line)
