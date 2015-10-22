# How to change the background color for tix.Balloon message?
b=Tix.Balloon(master,statusbar=statusbar)
for sub in b.subwidgets_all():
  sub.config(bg='grey')
