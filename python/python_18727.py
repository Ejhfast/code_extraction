# Add a legend in a 3D scatterplot with scatter() in Matplotlib
scatter1_proxy = matplotlib.lines.Line2D([0],[0], linestyle="none", c=colors[0], marker = 'o')
scatter2_proxy = matplotlib.lines.Line2D([0],[0], linestyle="none", c=colors[1], marker = 'v')
ax.legend([scatter1_proxy, scatter2_proxy], ['label1', 'label2'], numpoints = 1)
