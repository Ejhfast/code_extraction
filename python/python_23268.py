# Efficiently update values held in scoring matrix
scoring_matrix += (data_random &gt;= data_sorted).astype(int)
