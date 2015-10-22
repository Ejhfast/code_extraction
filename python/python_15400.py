# Inform OS of installation
import psutil
for p in psutil.process_iter():
    print p.name
