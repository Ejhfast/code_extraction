# Create Pandas Dataframe with loop
d = {'x' + str(i) : CRSP_mom[(CRSP_mom['mom_rank'] &gt; (float(i)-1.0)/10) &amp; (CRSP_mom['mom_rank'] &lt;= (float(i))/10)] for i in range(1, 11)}
