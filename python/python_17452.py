# Hide unselected in Maya/Python
cmds.hide(cmds.ls(lights=True, dag=True))
cmds.showHidden()
