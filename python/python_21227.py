# How do I get dimension data from Analytics reporting api
res = service.data().ga().get(ids='ga:' + profile_id, start_date='2014-01-01', end_date=t, metrics='ga:sessions', dimensions='ga:browser',sort='-ga:sessions' , max_results='5' ).execute()
