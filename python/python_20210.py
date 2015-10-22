# Evenlet semaphore, how to limit calls to a particular subprocess?
user -&gt; gunicorn (any number of processes)
gunicorn -&gt; one subprocess manager
manager -&gt; N subprocesses
