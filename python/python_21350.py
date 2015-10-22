# Change cell size in python wx widget
sizer = wx.BoxSizer(wx.VERTICAL)
sizer.Add(myWidget, proportion=1, flag=wx.EXPAND|wx.ALL, border=5)
sizer.Add(myOtherWidget, proportion=0, flag=wx.ALL, border=5)
