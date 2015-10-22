# How to know if it is unsigned of a field from mysql by MySQLdb
SELECT COLUMN_NAME, COLUMN_TYPE
  FROM INFORMATION_SCHEMA.COLUMNS
  WHERE table_name = 'tbl_name'
