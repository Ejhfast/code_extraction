# how to filter for objects with time
results.filter('created &gt; ', now - datetime.timedelta(days=2))
