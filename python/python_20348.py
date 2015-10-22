# python sqlalchemy exist & select 'next' syntax
from sqlalchemy.sql import func
# ...
~exist(func.next_value()).where(...)
