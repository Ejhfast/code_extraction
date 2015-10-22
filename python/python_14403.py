# grep logfile for a specific timeframe
awk -F'.' -vs="$start_time" -ve="$end_time" '$1&gt;s &amp;&amp; $1&lt;e' logfile
