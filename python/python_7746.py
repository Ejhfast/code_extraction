# Strange wx.CheckBox drawing in wx.ToolBar
self.tb.AddCheckLabelTool(id, hint, pic.GetBitmap(), shortHelp=hint)
self.tb.ToggleTool(id, self.grid.Table.actualOnly)
self.Bind(wx.EVT_TOOL, proc, id=id)
