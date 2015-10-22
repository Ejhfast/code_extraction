# Legend marker transparency - Matplotlit
marker_min = plt.Line2D((0, 0), (0, 0), markeredgecolor=(0.5, 0.0, 0.0), markerfacecolor='none', linestyle='', marker='x', markeredgewidth=2, markersize=5)
marker_max = plt.Line2D((0, 0), (0, 0), markeredgecolor=(0.0, 0.5, 0.0), markerfacecolor='none', linestyle='', marker='o', markeredgewidth=2, markersize=5)
plt.legend([marker_min, marker_max], ['Min Points', 'Max Points'], numpoints=1, loc='center left', bbox_to_anchor=(1, 0.5))
