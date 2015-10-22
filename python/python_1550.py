# Copy Table data from one DB to another
pg_dump -Fc db1 | pg_restore -d db2 -c
