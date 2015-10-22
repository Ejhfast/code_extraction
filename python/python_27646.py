# Setting values in grouped data frame in pandas
test.loc[g_test.get_group((1, 5, 13, 8)).index, 'monthly_sales'] = \
           g_train.get_group((1, 5, 13, 8)).monthly_sales.mean()
