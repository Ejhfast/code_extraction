# Constrain Mayavi mouse drag to rotating Earth around its axis
from tvtk.api import tvtk
fig = mlab.gcf()
fig.scene.interactor.interactor_style = tvtk.InteractorStyleTerrain()
