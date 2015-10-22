# Select a distinct column with it's relative id
select * from table1
 where id in (select min(id) from table1 group by `value`)
