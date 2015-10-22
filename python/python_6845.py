# Efficient way to format string
"select %(tableName)s.somefield, count(*) from %(tableName)s WHERE %(tableName)s.TimeStamp &gt; %(fromDate)s and %(tableName)s.EndTimeStamp &lt; %(to_data)s group by %(tableName)s.ProviderUsername;" %{'tableName':tableName, 'fromDate':fromDate, 'to_data':to_data}
