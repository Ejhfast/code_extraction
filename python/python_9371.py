# How to get process PID for manual lock mechanism in Python?
open(lock, 'w').write(os.getpid())
