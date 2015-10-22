# Keep order while using multiprocessing in Python
r = pool.map_async(...)
  r.wait()
