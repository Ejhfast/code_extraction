# wxPython: Items in BoxSizer don't expand horizontally, only vertically
sizer = wx.BoxSizer(wx.VERTICAL)
sizer.Add(widget1, 0, wx.EXPAND)
sizer.Add(widget2, 1)
