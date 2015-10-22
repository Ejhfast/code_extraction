# how do you connect to oracle using pyodbc
import pyodbc
connectString = 'Driver={Microdsoft ODBC for Oracle};Server=&lt;host&gt;:&lt;port&gt;/&lt;db&gt;.&lt;host&gt;;uid= &lt;username&gt;;pwd=&lt;password&gt;'
cnxn = pyodbc.connect(connectString)
