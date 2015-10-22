# Replacing missing data in pandas.DataFrame not working
j = df_train.IsAlone.astype(bool) &amp; df_train.Age.isnull()
i = df_train.IsAlone.astype(bool) &amp; ~df_train.Age.isnull()
df_train.loc[j, 'Age'] = df_train.loc[i, 'Age'].mean()
