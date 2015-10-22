# How to extract a plane from a 3D variable in FiPy (3D to 2D)
var2D.setValue(var3D((x2D, y2D,
                      zcut * ones(var2D.mesh.numberOfCells) + dx/2.), order=0))
