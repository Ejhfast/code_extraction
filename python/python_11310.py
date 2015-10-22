# COM objects (arcobjects) in Python
pGraphContLayout = CType(pLayout, esriCarto.IGraphicsContainer)
pFrame = pGraphContLayout.FindFrame(pMxDoc.ActiveView.FocusMap)
pGrids = CType(pFrame, IMapGrids)
