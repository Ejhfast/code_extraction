# Can I use a lambda expression here (selecting records from a numpy.core.records.recarray)?
[dt, val for dt, val in zip(date2num(r['dt'], r['val'])) if '2000-01-01' &lt; r['dt'] &lt; '2000-03-01']
