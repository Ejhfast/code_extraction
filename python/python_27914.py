# Seaborn: how to set bar borders' line width or color?
fig, ax = plt.subplots()
ax = sns.barplot(data = data, x = 'var1', color = '#007b7f')
plt.setp(ax.patches, linewidth=0)
