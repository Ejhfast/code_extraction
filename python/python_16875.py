# Doing simple Bash file write in Python
with open(COUNT_FILE, 'w') as f:
    f.write(str(int(COUNT)+1)+'\n')
