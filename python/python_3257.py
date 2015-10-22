# How to align 2 toolbars on same the row, one aligned left and one aligned right?
topToolBar.Add(toolbar1,1,wx.ALIGN_LEFT,4) # note the 2nd param 'proportion' is 1
#topToolBar.AddStretchSpacer()
topToolBar.Add(toolbar1,0,wx.ALIGN_RIGHT,4)
