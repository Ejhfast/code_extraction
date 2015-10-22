# How to stop a coroutines / thread in Python eventlet
while not q.empty():
    pool.spawn_n(download, q.get())
    if q.empty(): pool.waitall()
