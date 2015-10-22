# Python subprocess.Popen - adding GCC flags results in "no input files" error
p = Popen(['gcc', '-o', 'hello', 'hello.c'], stdout=subprocess.PIPE, stderr=stderr=subprocess.STDOUT)
