# Optimizing Python script that executes SQL
insert = "INSERT INTO test9 (field1, field2, field3) VALUES(?, ?, ?)"
c.execute(insert, [value1, value2, value3])
