# Group strings together and calculate total python
select emailaddress, sum(number) as total
from t
group by emailaddress
