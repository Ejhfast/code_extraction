# Create MySQL view with an extra calculated field in table
select *,TIME_TO_SEC(TIMEDIFF(NOW(), latest_time_seen)) as secs_diff from tbl
