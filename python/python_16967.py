# Pytz common timezones sorted by offset
&gt;&gt;&gt; tz = [(item, datetime.datetime.now(pytz.timezone(item)).strftime('%z') + " " + item) for item in pytz.common_timezones]
&gt;&gt;&gt; sorted(tz, key=lambda x: int(x[1].split()[0]))
[('Pacific/Midway', '-1100 Pacific/Midway'), ('Pacific/Niue', '-1100 Pacific/Niue'), ('Pacific/Pago_Pago', '-1100 Pacific/Pago_Pago'), ('Pacific/Honolulu', '-1000 Pacific/Honolulu'), ...
