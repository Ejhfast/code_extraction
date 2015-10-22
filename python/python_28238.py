# Python SQLite3 Mac Address with colons lookup
"SELECT mac_addr, timestamp, (SELECT COUNT(*) FROM mytblname AS t2 WHERE t2.mac_addr &lt;= t1.mac_addr) AS row_Num FROM mytblname AS t1 ORDER BY timestamp, mac_addr;"
