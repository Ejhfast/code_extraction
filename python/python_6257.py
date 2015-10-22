# How to get chars that are actually displayed in wx.TextCtrl?
from win32api import SendMessage
result = SendMessage(self.GetHandle(), EM_POSFROMCHAR, 0, 0)
