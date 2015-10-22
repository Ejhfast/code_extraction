# wxpython: How do we remove null byte from string when using textcontrol.GetValue()
cmd = self.tc1.GetValue().encode('ascii')
