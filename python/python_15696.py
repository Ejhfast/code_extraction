# Watch all system processes in Python
{process.pid: process.exe for process in psutil.process_iter() if process.pid}
