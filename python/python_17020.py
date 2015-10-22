# Identifying python processes
for p in psutil.get_process_list():
  if p.cmdline[0].endswith('pythonw.exe') and p.cmdline[1] == 'myscript.py':
    print p.pid
