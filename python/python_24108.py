# How to manage wx.StatusBar text in interactions with menus
self.CreateStatusBar(2)
self.SetStatusText("A Custom StatusBar...", 1)
wx.CallLater(10000, self.SetStatusText, "", 1)
