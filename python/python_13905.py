# Render output of Pandas 'to_latex' method in a matplotlib plot
ltx = a.to_latex().replace('\n', ' ')
plt.text(9, 3.4, ltx, size=12)
