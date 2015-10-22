# Celery rate_limit affecting multiple tasks
celeryd &lt;other opts&gt; -Q:fast fast_queue c:fast 5 -Q:slow slow_queue -c:slow 1
