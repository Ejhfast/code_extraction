# Pig - Python UDF issue
log = LOAD 'test.txt' USING PigStorage(',') AS (x:int);
db = LOAD 'data.mmdb' AS (entry:(field_1:chararray, field_2....));
result = FOREACH log GENERATE myudf.function(x, db.entry);
