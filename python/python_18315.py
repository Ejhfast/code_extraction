# Python Image object to WxPython
myWxImage = wx.ImageFromBuffer( imgobj.size[0], imgobj.size[1], imgobj.tostring() )
