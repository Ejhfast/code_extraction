# how to run vcvarsall.bat from python subprocess
subprocess.Popen('"vcvarsall.bat" x86&amp;&amp;"invoke_compiler.bat"', shell=True)
