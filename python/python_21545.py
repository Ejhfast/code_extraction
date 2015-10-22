# Insert Python datetime to Oracle column of type DATE
insert into x
values(99, to_date('2010/01/26:11:00:00AM', 'yyyy/mm/dd:hh:mi:ssam'));
