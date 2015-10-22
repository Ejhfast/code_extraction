# Matplotlib add a specific tick presenting axis max - multiple scales single observation
tcks = nax.get_yticks()
tcks[-1] = vmax
nax.set_yticks(tcks)
