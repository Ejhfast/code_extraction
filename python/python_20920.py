# Add a figure object to AxesSubplot Gridspec
phyl_ax=plt.subplot(gs[0])
Phylo.draw(tree, axes=phyl_ax)
