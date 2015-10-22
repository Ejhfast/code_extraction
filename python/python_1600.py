# Group by hour in SQLAlchemy?
query(extract('hour', timeStamp).label('h')).group_by('h')
