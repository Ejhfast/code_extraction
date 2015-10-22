# determine a boolean value based on min and max value
statement1='UPDATE table2 SET column= false WHERE value &gt;= (SELECT min FROM table1 WHERE
 table1.common_name=table2.common_name) AND value &lt;=(SELECT max FROM table1 WHERE
 table1.common_name=table2.common_name)'
