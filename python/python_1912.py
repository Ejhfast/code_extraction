# Is it possible to delete/remove a wx.aui.AuiManager pane?
manager.DetachPane(pane)
pane.Destroy()
manager.Update()
