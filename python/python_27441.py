# Maya Python: Check to see if the attribute has any keyframes
if cmds.keyframe(oldObjPath, attribute=oldAttr, sl=False, q=True, tc=True):
