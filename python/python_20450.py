# Show "Heat Map" image with alpha values - Matplotlib / Python
uncertainty = plt.cm.jet(data_property.data)
uncertainty[..., 3] = data_uncertainty.data
