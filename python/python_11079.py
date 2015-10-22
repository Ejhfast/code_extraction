# MultiLevel index to columns : getting value_counts as columns in pandas
dfgb['bar'].value_counts().unstack().fillna(0.)
