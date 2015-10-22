# Find indices based on datetime
np.where(date_list == np.datetime64(datetime.datetime(2015, 3, 31)))
&gt;&gt;&gt; (array([ 63, 356, 649], dtype=int64),)
