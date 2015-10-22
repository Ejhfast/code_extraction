# Building correct MySQL datetime formatted string for yesterday in Python
(datetime.now() - timedelta(hours=24)).strftime('%Y-%m-%d %H:%M:%S')
