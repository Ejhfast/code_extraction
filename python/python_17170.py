# How to find all upstream DG nodes with maya python api?
import maya.cmds as cmds
 cmds.ls(*cmds.listHistory (mynode), type = 'animCurve' )
