# Name of files opened by a process in window?
import psutil
   p = psutil.Process(os.getpid()) # or PID of process
   p.open_files()
