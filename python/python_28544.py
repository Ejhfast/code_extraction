# My None check is not working keep getting "NoneType object has no attribute XXX"
childMbo = childSet.getMbo(0)
if childMbo is not None:
    childassetnum = childMbo.getString('ASSETNUM')
