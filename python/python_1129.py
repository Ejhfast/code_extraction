# How do I embed IPython with working generator expressions?
import IPython.Shell
ipshell = IPython.Shell.IPShell(argv=[], user_ns={'root':root})
ipshell.mainloop()
