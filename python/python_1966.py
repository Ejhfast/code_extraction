# How can I draw to a MemoryDC using the GraphicsContext, and then blit that to a PaintDC?
bitmap = wx.EmptyBitmap(w, h)
dc = wx.MemoryDC(bitmap)
