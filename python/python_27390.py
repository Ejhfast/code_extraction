# Escaping string arugments to subprocess calls in Windows
p = subprocess.Popen('clip.exe', stdin=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
p.communicate('hello \n world')
p.wait()
