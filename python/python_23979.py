# Using an integer as an SQL Alchemy selectable
select([table.c.id, table.c.value, literal("1").label("new_column")])
