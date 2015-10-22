# Silencing warnings in Pandas
mydf = pd.read_csv(p_file, sep=',', error_bad_lines=False, index_col=False, warn_bad_lines=False)
