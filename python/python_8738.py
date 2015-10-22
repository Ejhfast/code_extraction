# Shell piping with subprocess in Python
pipe = Popen(command_2, shell=True, stdin=PIPE, stdout=PIPE)
pipe.stdin.write(result_1)
pipe.communicate()
