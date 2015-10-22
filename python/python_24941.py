# Matplotlib scatter plot different colors in legend and plot
c = next(colors)
ax.errorbar(df2a['x_var_plot'],  df2a[col], color = c, yerr=df2a_err[col], fmt='o')
ax.scatter(df2a['x_var_plot'], df2a[col], color = c, label=col)
