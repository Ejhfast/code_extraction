# set axis limits on individual facets of seaborn facetgrid
g = sns.FacetGrid(mapping, col=options.facetCol, row=options.facetRow, col_order=sorted(cols), hue=options.group, sharex=False)
