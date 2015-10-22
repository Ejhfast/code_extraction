# In which encoding does the shell command [mysql -e "..." -u ... > some_file.sql] store the content into some_file.sql?
mysql --default-character-set=utf-8 -e "SELECT some, thing FROM some_where" -u my_user -p my_database &gt; some_file.sql
