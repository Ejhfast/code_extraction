# Plotting isosurface with Mayavi of irregularly spaced data
src = mlab.pipeline.scalar_scatter(x,y,z,s)
iso=mlab.pipeline.iso_surface(gs)
