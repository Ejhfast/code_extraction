# Prevent matplotlib from interpreting underscore as subscript in plot title
title = 'I_hate_subscripts'
title = title.replace('_', '\_')
plt.title(title)
