# wx slider binding function returns twice
self.slider.Bind(wx.EVT_COMMAND_SCROLL_THUMBTRACK, self.sliderUpdate)
self.slider.Bind(wx.EVT_COMMAND_SCROLL_CHANGED, self.sliderUpdate)
