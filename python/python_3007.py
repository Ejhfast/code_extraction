# wxPython GridSizer.Add() not working for custom control
class ReaderControl(wx.richtext.RichTextCtrl):
    def __init__(self, parent, id=-1, value=''):
        wx.richtext.RichTextCtrl.__init__(self, parent, id, value, style=wx.richtext.RE_READONLY, name='ReaderControl'
