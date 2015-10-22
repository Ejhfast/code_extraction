# How to make Wxpython NewWindow appear to the Top
class NewWindow(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, size=(400,250), style=wx.DEFAULT_FRAME_STYLE| wx.STAY_ON_TOP)
