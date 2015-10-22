# column names on grouped DataFrame output to CSV
group_df = df.groupby(group_name).agg([np.mean, np.std, np.count_nonzero])
group_df.rename(None, lambda coltuple: '_'.join(coltuple), False, True)
