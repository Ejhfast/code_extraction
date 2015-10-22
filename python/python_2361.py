# wxpython Prevent Ctrl+Enter from changing the focus
ac = [(wx.ACCEL_CTRL, wx.WXK_RETURN, wx.NewId())]
    tbl = wx.AcceleratorTable(ac)
    list.SetAcceleratorTable(tbl)  # should overwrite its bindings?
