# Close pdf-file or exe-application from Python
for p in psutil.process_iter():
    if p.name == 'calc.exe':
        p.kill()
