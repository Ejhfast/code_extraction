# How to display a given number of colors in a matplotlib contourf and colorbar
plt.contourf(np.array([[1.0, 1.5, 2.0, 2.5, 3.0], [3.5, 4.0, 4.5, 5.0, 5.0]]), cmap=cmap, levels = np.linspace(1.0, 5.0, 6))
