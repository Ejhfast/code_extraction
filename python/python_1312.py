# wxPython wxDC object from win32gui.GetDC
window = wx.Frame(None, -1, '')
window.AssociateHandle(hwnd)
dc = wx.WindowDC(window)
