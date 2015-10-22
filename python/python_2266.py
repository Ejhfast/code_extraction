# Getting a RichTextCtrl's default font size in wxPython
self.defaultstyle = wx.richtext.RichTextAttr()
self.GetStyle(self.GetInsertionPoint(), self.defaultstyle)
self.defaultsize = self.defaultstyle.GetFont().GetPointSize()
