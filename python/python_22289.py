# Cycle colors when plotting in matplotlib: Tracking state on a per-instance basis
def next_color(self):
    return next(self._get_lines.color_cycle)
plt.Axes.next_color = next_color
