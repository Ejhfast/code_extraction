# Exit frame and panel from panel method
def onClose(self, event):
   frame = self.GetParent()
   frame.Close()
