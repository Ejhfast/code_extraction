# mysql service start time
select date_sub(now(), INTERVAL variable_value SECOND) started_at
from information_schema.global_status
where variable_name='Uptime';
