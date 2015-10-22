# Using \o command within a script
echo "\o test.out \\ select * from test;" | psql -wU user db_name
