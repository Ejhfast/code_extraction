# Why do sns.lmplot and FacetGrid+plt.scatter create different scatter points from the same data?
fig1 = sns.lmplot("Av_density", "pred2", Data, col="LOC", hue="YEAR", col_wrap=2);
fig1.set(ylim=(-0.03, 0.05))
plt.show(fig1)
