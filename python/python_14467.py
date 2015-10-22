# Merging whilst keeping order in R and pandas
Ordered.reset_index().merge(Ordered, Unordered, on=ByWhatColumn).set_index('index')
