# Python: get output of the shell command 'history'
for history in open('/home/user/.bash_history):
    print(history, end='')
