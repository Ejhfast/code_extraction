# Unable to import 3.4GB csv into redshift because values contains free-text with commas
cast(left(column_name, 10)||' '||right(column_name, 6)||':00' as timestamp)
