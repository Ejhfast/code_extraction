# Showing a .png image in a window in wxPython
png = wx.Image(imageFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
wx.StaticBitmap(self, -1, png, (10, 5), (png.GetWidth(), png.GetHeight()))
