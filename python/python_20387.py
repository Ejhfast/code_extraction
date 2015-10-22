# maya python print state of checkbox?
def GetSelectedNodes(self,*args):
    cal = cmds.checkBox(self.xAxis,q = True, v = True)
    print cal
