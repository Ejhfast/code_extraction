# Maya useRayTraceShadows - Python error NoneType object is not iterable
selectedLights = cmds.textScrollList ("lgtList", query = True,
                                      selectItem = True) or []
