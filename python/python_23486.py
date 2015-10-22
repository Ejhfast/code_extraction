# Python - Fastest way to update multiple records in one table by selecting id from B table
UPDATE tableB SET column2 = tableA.column2 WHERE tableB.column1 = tableA.column1
