# How to hide PPT presentation using com/ironPython
if self.isVisible:
    self.com_app.Visible = self.isVisible
com_ppt = self.com_app.Presentations.Open(filename, WithWindow = isVisible)
