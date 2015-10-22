# matplotlib: get projection coordinates
x2, y2, _ = proj3d.proj_transform(x1,y1,z1, ax.get_proj())
