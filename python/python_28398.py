# flask-sqlalchemy, sql count records in a relationship and then join to a users table
select users.*, count(*) over (partition by friendship.user)
from users inner join friendship on users.id = friendship.user
order by count
