# Will dumping, creating a new database, and then restoring Django auth and system related tables cause any problems?
mysqldump -uusername -ppassword db_name table_name &gt; xxxx.sql
mysql -uusername -ppassword new_db_name &lt; xxxx.sql
