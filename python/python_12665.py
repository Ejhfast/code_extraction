# python open large log file
with open("/opt/CLiMB/Storage1/log/vsftp.log") as f:
     f.seek(-1000, os.SEEK_END)
     print f.read()
