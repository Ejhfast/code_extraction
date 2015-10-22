# Handling newlines within sed; command called from Python
cmd = r'cat /proc/cpuinfo | egrep "core id|physical id" | tr -d "\n" | sed -e s/ph/\\nPH/g | grep -v ^$ '
