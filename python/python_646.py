# wxPython: Making something expand
sizer = wx.BoxSizer(wx.VERTICAL)
sizer.Add(self.canvas, 1, wx.EXPAND)
self.SetSizer(sizer)
