# Retrieving values from a list of dictionaries
&gt;&gt;&gt; next(consumer['api_key'] for consumer in API_CONSUMERS if consumer['host'] == host)
'Ahth2ea5Ohngoop5'
