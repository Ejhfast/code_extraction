# Pandas scatter_matrix - plot categorical variables
df['Sex_int'] = np.nan
df.loc[df['Sex'] == 'M', 'Sex_int'] = 0
df.loc[df['Sex'] == 'F', 'Sex_int'] = 1
