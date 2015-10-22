# psycopg - Get formatted sql instead of executing
SQLstring = curs.mogrify('select name, age from people where name = %s;', ('ann',) )
